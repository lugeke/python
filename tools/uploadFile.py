import concurrent.futures
import logging
import os
import time
from queue import Queue

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path=r'/Applications/chromedriver', options=chrome_options)  

logging.basicConfig(filename='upload.log', format='%(asctime)s %(message)s', level=logging.INFO)
queue = Queue()


movies_ext = ('.mp4', '.wmv', '.mkv', )


def scan_dir(dir_path):
    filename_set = set()
    while True:
        files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and not f.startswith('.')]
        movie_files = [f for f in files if f.endswith(movies_ext)]

        for f in movie_files:
            if f in filename_set:
                continue
            filename_set.add(f)
            cover_file = os.path.join(dir_path, f'{os.path.splitext(f)[0]}.jpg')
            if not os.path.exists(cover_file):
                cover_file = ''
            queue.put({
                'movieFile': os.path.join(dir_path, f),
                'coverFile': cover_file,
            })
            logging.info(f'queue put {f}')
                    
        logging.info('*')
        time.sleep(60)


def run_thread_pool(dir_path):
    logging.info('runThreadPool')
    # We can use a with statement to ensure threads are cleaned up promptly
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # Start the load operations and mark each future with its index
        executor.submit(scan_dir, dir_path)
        executor.submit(fill_form_upload)


def login_to_upload():
    driver.get('https://avgle.com/upload/video') 

    time.sleep(3)
    driver.find_elements_by_name('username')[1].send_keys('loverio')
    driver.find_elements_by_name('password')[1].send_keys('avgleljh')
    driver.find_elements_by_name('submit_login')[1].click()
    time.sleep(2)


def fill_form_upload():
    last_upload_file = ''
    while True:
        try:
            if driver.find_element_by_id('upload_video_submit').get_attribute('value') == \
                    'I declare this is not Child Porn. Upload':
                if os.path.exists(last_upload_file):
                    # os.remove(last_upload_file)
                    logging.info(f'end upload {last_upload_file}')
                file_info = queue.get()
                movie_file = file_info['movie_file']
                cover_file = file_info['cover_file']
                logging.info(f'begin upload {movie_file}')
                last_upload_file = movie_file
                title = os.path.basename(movie_file)[:-4]
                tags = os.path.basename(os.path.dirname(movie_file))
                driver.find_element_by_id('upload_video_title').send_keys(title)
                driver.find_element_by_id('upload_video_keywords').send_keys(tags)
                # driver.find_element_by_id('upload_video_category').selectedIndex = 19 //15
                driver.execute_script("document.getElementById('upload_video_category').selectedIndex = 15")
                driver.find_element_by_id('upload_video_privacy_private').click()
                driver.find_element_by_id('upload_video_password').send_keys('riorio')
                driver.find_element_by_id('upload_video_file').send_keys(movie_file)
                if cover_file:
                    driver.find_element_by_id('upload_video_thumb').send_keys(cover_file)
                driver.find_element_by_id('upload_video_submit').click()
            else:
                time.sleep(60)
                logging.info('-')
        except Exception as e:
            logging.info(f'error {e}')
            driver.quit()
            login_to_upload()


if __name__ == '__main__': 
    dirPath = r'/Volumes/tv/Abstract.The.Art.of.Design.S01.mp4/rio' 
    login_to_upload()
    run_thread_pool(dirPath)
    driver.quit()
    logging.info('complete')
