import requests
from bs4 import BeautifulSoup
import re
url = 'https://www.seedmm.com/star/n4r'


def get_movie_links(url, end):
    for i in range(1, end+1):
        page = requests.get('%s/%d' % (url, i)).text
        soup = BeautifulSoup(page, 'html.parser')
        for tag in soup.find_all(class_='movie-box'):
            yield tag['href']


# https://btso.pw/search/MEYD-063 ->
def toMagnets(url):
    response = requests.get(url)
    page = response.text
    soup = BeautifulSoup(page, 'html.parser')
    magnets = []
    for a in soup.find_all('a', href=re.compile('https://btso.pw/magnet/detail/hash/')):
        magnet = a['href'].split('/')[-1]
        size = a.findChildren('div')[1].text
        magnets.append((magnet, size))
    return magnets


print(toMagnets('https://btso.pw/search/MEYD-063'))

# for movie_link in get_movie_links(url, 2):
#     print(movie_link)
# for magnet in get_magnets('https://www.seedmm.com/MEYD-262'):
#     print(magnet)
