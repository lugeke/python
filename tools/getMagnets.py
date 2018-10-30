import requests
from bs4 import BeautifulSoup
import re
from collections import namedtuple

# html => content
url = 'https://www.bthuahua.net/index.php'

MagnetURI = namedtuple('MagnetURI', ['name', 'hashcode', 'size'])

def html_generator(url, start=1, end=100):
    kw = 'Riley Reyes rarbg 1080p'
    for p in range(start, end+1):
        params = {'r': 'files/index', 'kw': kw, 'page': p}
        yield requests.get(url, params=params).text

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

htmls = html_generator(url)
contents = content_generator(htmls)

for m in contents:
    print(m.hashcode)
