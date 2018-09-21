#coding=utf-8
from selenium import webdriver
import time

values=['selenium','webdriver',u'虫师']
for serch in values:
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(serch)
time.sleep(3)
