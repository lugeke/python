#import urllib.request
import types
from  bs4 import BeautifulSoup
import urllib.request
import bs4
import re
import time
def get_page(url):
	#time.sleep(30)
	# headers = {
	# 'Connection': 'Keep-Alive',
	# 'Accept': 'text/html, application/xhtml+xml, */*',
	# 'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
	# 'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'}
	headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
	print('request %s' %(url))
	req = urllib.request.Request(url=url,headers=headers) 
	page = urllib.request.urlopen(req).read()
	return page

# url = 'http://www.javhip.com/cn/star/2jv'
def get_movie_links(url):
	page= get_page(url)
	soup = BeautifulSoup(page,'html.parser')
	for tag in soup.find_all(class_ = 'movie-box'):
		yield tag['href']


def test_get_movie_links():
	url = 'http://www.avmoo.net/cn/star/cnw/currentPage/1'
	for link in get_movie_links(url):
		print(link)


#test_get_movie_links()
 

def isCollection(tag):
	return tag and tag.name == 'span' and tag.has_attr('class') and tag['class'][0] == 'genre' and tag.text == '合集'



def get_bt_links(url):
	def to_bt_link(url):
		page = get_page(url)
		soup = BeautifulSoup(page,'html.parser')
		if not soup.find(isCollection):
			tag = soup.find('a',href = re.compile('http://www.btaia.com/search/'))
			if tag:
				return tag['href']
	for movie_link in get_movie_links(url):
		link = to_bt_link(movie_link)
		if link: yield link


def test_get_bt_links():
	url = 'http://www.avmoo.net/cn/star/cnw/currentPage/1'
	for bt_link in get_bt_links(url):
		print(bt_link)

#test_get_bt_links()

def get_Magnet(url):
	time.sleep(10)
	page = get_page(url) 
	soup = BeautifulSoup(page,'html.parser')
	result = False
	magnetLink = ''
	files=soup.find_all('div',class_='file')
	play_set = set(['avi','rmvb','rm','asf','mpg','mp4','wmv','mkv'])
	for f in files:
		ext = f.text.split('.')[-1].lower()
		if ext and (ext in play_set):
			#magnetLink = soup.find('textarea',id='magnetLink').text
			magnetLink = 'magnet:?xt=urn:btih:' + url.split('/')[-1]
			result = True
			break
	return (result,magnetLink)

def test_get_magnet():
	url = 'http://www.btaia.com/magnet/detail/hash/4FA5B14FB017640BE602BF657053FB3BF73492DE'
	print(get_Magnet(url))

#test_get_magnet()


# http://www.btaia.com/search/AVOP-144  ->
def toMagnet(url):
	page = get_page(url)
	soup = BeautifulSoup(page,'html.parser')
	max_size = 0
	max_link = ''
	for tag in soup.find_all('a',href = re.compile('http://www.btaia.com/magnet/detail/hash/')):
		link = tag['href']
		size = tag.findChildren('div')[1].text
		#print(size)
		pattern = re.compile('Size:(\d+\.?\d*)(\w+)')
		match = pattern.match(size)
		if match:
			size = float(match.group(1))
			if match.group(2) == 'MB':
				size /= 1024
			#print(size)
			canplay,magnetLink = get_Magnet(link)
			if size > max_size and canplay:
				max_size = size
				max_link = magnetLink
	#print(max_size)
	return max_link


def test_toMagnet():
	url = 'http://www.btaia.com/search/AVOP-144'
	print(toMagnet(url))

#test_toMagnet()

def get_magnets(url):
	try:
		f = open(url.split('/')[-1]+'.txt','w')
		for bt_link in get_bt_links(url):
			magnetLink = toMagnet(bt_link)
			if magnetLink != '':
				#yield magnetLink
				print(magnetLink,file = f)
	except Exception as e:
		print('url error %s %s' %(bt_link, e))
	finally:
		f.close()

def test_get_magnets():
	url = 'http://www.avmoo.net/cn/star/cnw/currentPage/6'
	get_magnets(url)

test_get_magnets()


import threading

class crawThread(threading.Thread):
	def __init__(self,url):
		threading.Thread.__init__(self)
		#self.deamon = True
		self.url = url
	def run(self):
		f = open(url.split('/')[-1]+'.txt','w')
		for bt_link in get_bt_links(url):
			magnetLink = toMagnet(bt_link)
			if magnetLink != '':
				#yield magnetLink
				print(magnetLink,file = f)
		f.close()


# urlBase = 'http://www.javmoo.xyz/cn/star/cnw' + '/currentPage/'
# for i in range(2):
# 	url = urlBase+str((i+1))
# 	print(url)
# 	get_magnets(url)