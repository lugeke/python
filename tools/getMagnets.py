import requests
from bs4 import BeautifulSoup
url = 'https://www.seedmm.com/star/n4r'


def get_movie_links(url, end):
    for i in range(1, end+1):
        page = requests.get('%s/%d' % (url, i)).text
        soup = BeautifulSoup(page, 'html.parser')
        for tag in soup.find_all(class_='movie-box'):
            yield tag['href']


def get_magnets(link):
    page = requests.get(link).text
    soup = BeautifulSoup(page, 'html.parser')
    soup._select_debug = True
    trs = soup.select('table#magnet-table > tr')
    magnets = []
    for tr in trs:
        magnet = tr.select('td:nth-of-type(1) a').get('href')
        size = tr.select('td:nth-of-type(2) a').get_text()
        magnets.append((magnet, size))
    return magnets


# for movie_link in get_movie_links(url, 2):
#     print(movie_link)
for magnet in get_magnets('https://www.seedmm.com/MEYD-262'):
    print(magnet)
