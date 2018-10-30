import requests
from bs4 import BeautifulSoup
import re
from collections import namedtuple
import urllib
# url => html => content
url = 'https://www.bthuahua.net/index.php?r=files%2Findex&kw=Riley+Reyes+rarbg+1080p&page={}'
# url = 'https://bt2.bt87.cc/index.php?r=files%2Findex&kw=Nina+Skye+rarbg+1080p&page={}'

MagnetURI = namedtuple('MagnetURI', ['name', 'hashcode', 'size'])

def url_generator(url, start=1, end=100):
    for i in range(start, end+1):
        yield url.format(i)

def html_generator(urls):
    for url in urls:
        yield requests.get(url).text

def content_generator(htmls):
    for h in htmls:
        soup = BeautifulSoup(h, 'html.parser')
        lis = soup.find_all('li', class_='col-xs-12 list-group-item')
        if not lis: return
        for li in lis:
            hashcode = 'magnet:?xt=urn:btih:{}'.format(li.a['href'][-40:])
            name = li.a.string
            size = li.find(class_='label label-warning').string
            magnet = MagnetURI(name, hashcode, size)
            yield magnet

urls = url_generator(url)
htmls = html_generator(urls)
contents = content_generator(htmls)


for m in contents:
    print(m.hashcode)
