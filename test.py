import unittest
import time

print("begin")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


xpaths = [r'//*[@id="js_main_nav_cloud"]',
r'//*[@id="js_cloud_nav"]/div[1]/div/div[1]/a',
r'//*[@id="js_data_list"]/div/ul/li[2]/span[1]/em/a[1]'
]

frames = ['', '', 'wangpan']
for i in range(0, len(frames)):
    print(i)
# for xpath in xpaths:
#     driver.find_element_by_xpath(xpath).click()
#     time.sleep(3)
# driver.switch_to_frame('wangpan')