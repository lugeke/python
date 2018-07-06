import requests
from bs4 import BeautifulSoup
import re

# url => html => content
url = 'https://bt2.bt87.cc/index.php?r=files%2Findex&kw=Natalia+Starr+rarbg+1080p&page={}'
def url_genetor(url, start, end):
    for i in range(start, end+1):
        yield url.format(i)

def html_genetor(urls):
    for url in urls:
        yield requests.get(url).text

def content_genetor(htmls):
    for h in htmls:
        soup = BeautifulSoup(h, 'html.parser')
        lis = soup.find_all('li', class_='col-xs-12 list-group-item')
        for li in lis:
            hashcode = 'magnet:?xt=urn:btih:{}'.format(li.a['href'][-40:])
            name = li.a.string
            size = li.find(class_='label label-warning').string
            yield (name, hashcode, size)
            

urls = url_genetor(url, 1, 10)
htmls = html_genetor(urls)
contents = content_genetor(htmls)
contents = list(contents)
print(contents)
