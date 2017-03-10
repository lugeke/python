import unittest
import time

print("begin")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://115.com")
time.sleep(10)
xpaths = [r'//*[@id="js_main_nav_cloud"]',
r'//*[@id="js_cloud_nav"]/div[1]/div/div[1]/a',
r'//*[@id="js_data_list"]/div/ul/li[2]/span[1]/em/a[1]',
r'//*[@id="js_data_list"]/div/ul/li[3]/span[1]/em/a[1]',
r'//*[@id="js_data_list"]/div/ul/li[21]/span[1]/em/a[1]',
r'//*[@id="js_data_list"]/div/ul/li[1]/span[1]/em/a[1]'
]

frames = ['', '', 'wangpan','','','']
for i in range(0, len(xpaths)):
    if frames[i] != '' : driver.switch_to_frame('wangpan')
    driver.find_element_by_xpath(xpaths[i]).click()
    time.sleep(3)
