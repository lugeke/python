import requests
from bs4 import BeautifulSoup
from collections import namedtuple
import os
from concurrent import futures
import abc
from selenium import webdriver
import time


def get_domin(url):
    from urllib.parse import urlparse
    parsed_uri = urlparse(url)
    domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
    return domain

def download(img, dest_dir):
    # print(img, dest_dir)
    response = requests.get(img)
    if response.status_code == 200:
        # print('response')
        with open(dest_dir, 'wb') as f:

            f.write(response.content)
    else:
        print("error status_code: {}".format(response.status_code))


def download_images(url_generator):
    with futures.ThreadPoolExecutor(max_workers=8) as executor:
        for image, file_name in url_generator:
            future = executor.submit(download, image, file_name)
            print("Scheduled for {}: {}".format(image.split("/")[-1], future))

class mangaGenerator:
    def __init__(self, url, save_dir, slice_):
        self.url = url
        self.save_dir = save_dir
        self.slice_ = slice_


    @abc.abstractmethod
    def parse_table(self):
        """parse manga table link, return links[slice]"""
        
    @abc.abstractmethod
    def parse_content(self, content):
        """parse singe content, return tuples of (image, file_path)"""


    def __iter__(self):
        for name, content in self.parse_table():
            image_dir = os.path.join(self.save_dir, name)
            os.makedirs(image_dir, exist_ok = True)

            for index, image in enumerate(self.parse_content(content), 1):
                # get suffix .jpg or .jpeg
                suffix = image.split(".")[-1]
                file_name = os.path.join(image_dir, '{:03d}.{}'.format(index, suffix))
                yield image, file_name


# https://www.bbdmw.com/cartoon/58
# 贝贝动漫
class BbdmMG(mangaGenerator):
    def parse_table(self):
        html = requests.get(self.url).text
        # html = requests.get('https://www.bbdmw.com/cartoon/58').text
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.select('.detail-list-select a')[self.slice_]
        for l in links: 
            yield l.text, "{}/{}".format(get_domin(self.url), l['href'])
    
    def parse_content(self, content):
        html = requests.get(content).text
        soup = BeautifulSoup(html, 'html.parser')
        images  = soup.find_all('img', class_='lazy')
        if not images: 
            print("cant't find img element ")
            return
        for image in images:
            # print(image)
            src = image['data-original']
            yield src


# https://hhmh5.com/?act=list&aid=70
# 哈哈动漫
class HhdmMG(mangaGenerator):

    def __init__(self, url, save_dir, slice_):
        super().__init__(url, save_dir, slice_)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        self.driver = webdriver.Chrome(executable_path=r'/Applications/chromedriver', options=chrome_options) 

    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.driver.quit()
    
    def parse_table(self):
        # driver.get('https://hhmh5.com/?act=list&aid=70')
        self.driver.get(self.url)
        time.sleep(2)
        links = self.driver.find_elements_by_css_selector("ul#html_box a")[self.slice_]
        links = [(l.find_element_by_class_name('pull-left').text, l.get_attribute('href')) for l in links]
        return links
    
    def parse_content(self, content):
        # driver.get('https://hhmh5.com/style.html?act=style&aid=70&cid=14443')
        self.driver.get(content)
        print('content', content)
        time.sleep(2)
        image  = self.driver.find_element_by_css_selector('img.lazy').get_attribute('data-original')
        # https://abc.yuyzf.com/files/80668/65265/2.jpg
        if not image: 
            print("cant't find img element ")
            return
        suffix = image.split(".")[-1]
        prefix = "/".join(image.split("/")[:-1])
        for i in range(1, 50):
            yield '{}/{}.{}'.format(prefix, i, suffix)
        

# start = 6
# end = 32
# download_images(BbdmMG(
#     'https://www.bbdmw.com/cartoon/58',
#     r'/Users/jiaheng/Downloads/漂亮乾姊姊',
#     slice(start-1, end)
# ))


start = 33
end = 39
with HhdmMG('https://hhmh5.com/?act=list&aid=70', r'/Users/jiaheng/Downloads/漂亮乾姊姊', slice(start-1, end)) as h:
    download_images(h)