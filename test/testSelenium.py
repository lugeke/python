import unittest
import time
import types
import collections
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

print("begin")

driver = webdriver.Chrome()
driver.get("http://115.com")

WebDriverWait(driver, 60).until(EC.title_contains('江湖'))


def click(xpaths):
    def _click(xpath):
        driver.find_element_by_xpath(xpath).click()
        time.sleep(3)
    if type(xpaths) is list:
        for xpath in xpaths:
            _click(xpath)
    else:
        _click(xpaths)


xpaths = [
    r'//*[@id="js_main_nav_cloud"]',
    r'//*[@id="js_cloud_nav"]/div[1]/div/div[1]/a'
]

# change to dest dir
click(xpaths)
driver.switch_to_frame('wangpan')

xpaths = [
    r'//*[@id="js_data_list"]/div/ul/li[2]/span[1]/em/a[1]',
    r'//*[@id="js_data_list"]/div/ul/li[3]/span[1]/em/a[1]',
]

click(xpaths)
dir_header = r'//*[@id="js_top_bar_box"]/div[2]/a[3]'


def iterate_page():
    item_template = r'//*[@id="js_data_list"]/div/ul/li[%d]/span[1]/em/a[1]'
    for i in range(4, 20):
        click(dir_header)
        try:
            click(item_template % (i))
            for j in range(1, 50):
                try:
                    click(item_template % (j))
                except Exception as e:
                    print('error %d, %d' % (i, j), end=" ")
        except Exception as e:
            print('error %d' % (i), end=" ")


iterate_page()
time.sleep(10)
# driver.quit()
