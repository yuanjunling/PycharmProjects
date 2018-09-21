#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep
#日期包
from  datetime  import  *
import unittest
import time , os
try:
    browser=webdriver.Chrome()
    browser.get("http://qa.egtcp.com/")
    browser.maximize_window()
    browser.find_element_by_link_text("Join Free").click()
except:
    browser.get_screenshot_as_file(u"D:/save_screenshot/%s.png" % datetime.now().strftime("%Y%m%d.%H%M%S.%f")[:-3])

try:
  browser.find_element_by_id("Email").send_keys("26141289@qq.com")
  browser.find_element_by_id("Password").send_keys("1234")
  browser.find_element_by_id("ConfirmPassword").send_keys("1234")
  browser.find_element_by_id("FirstName").send_keys("klfg")
  browser.find_element_by_id("LastName").send_keys("testy")
  browser.find_element_by_id("verifyCode").send_keys("greattao0818")
except:
    #给图片名称加上时间戳#
  browser.get_screenshot_as_file(u"D:/error/注册%s.png" % datetime.now().strftime("%Y.%m.%d.%H.%M.%S.%f")[:-3])

'''
time.time() 获取当前时间戳
time.localtime() 当前时间的 struct_time 形式
time.ctime() 当前时间的字符串形式
time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())'''