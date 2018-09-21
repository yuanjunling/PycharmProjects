#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time,login
import os,time
#open 方法以只读方式（r）打开本地的 data.txt 文件，readlines 方法是逐行的读取文件内容。
source=open("D:\\test01\\data0580.txt",'r')
values=source.readlines()
source.close()
# 通过 for 循环，serch 可以每次获取到文件中的一行数据，在定位到百度的输入框后，将数据传入
# send_keys(serch)。这样通过循环调用，直到文件的中的所有内容全被读取。
for serch in values:
    browser = webdriver.Chrome()
    browser.get("http://www.baidu.com")
    browser.find_element_by_id("kw").send_keys(serch)
    browser.find_element_by_id("su").click()
    time.sleep(3)
    browser.quit()




