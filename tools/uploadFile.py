import concurrent.futures
import json
import logging
import os
import re
import time
from queue import Queue

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path=r'/Applications/chromedriver', options=chrome_options)  

logging.basicConfig( format='%(asctime)s %(message)s', level=logging.INFO)
queue = Queue()


movies_ext = ('.mp4', '.wmv', '.mkv', )

def scan_Dir(dir_Path):
    filenameSet = set() 
    while True:
        files = [f for f in os.listdir(dir_Path) if os.path.isfile(os.path.join(dir_Path, f)) and not f.startswith('.')]
        movie_files = [f for f in files if f.endswith(movies_ext)]

        for f in movie_files:
            if f in filenameSet: continue
            filenameSet.add(f)
            cover_file = os.path.join(dir_Path, f'{os.path.splitext(f)[0]}.jpg')
            if not os.path.exists(cover_file): cover_file = ''
            queue.put({
                'movieFile': os.path.join(dir_Path, f),
                'coverFile': cover_file,
            })
            logging.info(f'queue put {f}')
                    
        logging.info('*')
        time.sleep(60)


def runThreadPool(dirPath):
    logging.info('runThreadPool')
    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its index
        executor.submit(scan_Dir, dirPath)
        executor.submit(fillFormAndUplaod)



def loginToUpload():
    driver.get('https://avgle.com/upload/video') 

    time.sleep(3)
    driver.find_elements_by_name('username')[1].send_keys('loverio')
    driver.find_elements_by_name('password')[1].send_keys('avgleljh')
    driver.find_elements_by_name('submit_login')[1].click()
    time.sleep(2)


def fillFormAndUplaod():
    lastUploadFile = ''
    while True:
        try:
            if driver.find_element_by_id('upload_video_submit').get_attribute('value')=='I declare this is not Child Porn. Upload':
                if os.path.exists(lastUploadFile):
                    # os.remove(lastUploadFile)
                    logging.info(f'end upload {lastUploadFile}')
                fileInfo = queue.get()
                movieFile = fileInfo['movieFile']
                coverFile = fileInfo['coverFile']
                logging.info(f'begin upload {movieFile}')
                lastUploadFile = movieFile
                title = os.path.basename(movieFile)[:-4]
                tags = os.path.basename(os.path.dirname(movieFile))
                driver.find_element_by_id('upload_video_title').send_keys(title)
                driver.find_element_by_id('upload_video_keywords').send_keys(tags)
                # driver.find_element_by_id('upload_video_category').selectedIndex = 19 //15
                driver.execute_script("document.getElementById('upload_video_category').selectedIndex = 15")

                driver.find_element_by_id('upload_video_privacy_private').click()
                driver.find_element_by_id('upload_video_file').send_keys(movieFile)
                if coverFile:
                    driver.find_element_by_id('upload_video_thumb').send_keys(coverFile)
                driver.find_element_by_id('upload_video_submit').click()
            else:
                time.sleep(60)
                logging.info('-')
        except Exception as e:
            print(e)
            driver.quit()


if __name__ == '__main__': 
    dirPath = r'/Volumes/tv/Abstract.The.Art.of.Design.S01.mp4/rio' 
    loginToUpload()
    runThreadPool(dirPath)
    driver.quit()
    logging.info('complete')
