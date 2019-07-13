#  -*- coding:utf-8 -*-

import os
import unittest
from appium import webdriver
from time import sleep
from random import choice
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time,random

def addcheckout(driver):
    time.sleep(3)
    driver.find_element_by_id("com.lab.testing:id/txt_inpsect").click()
    time.sleep(1.5)
    driver.find_element_by_name(u"导入历史纪录").click()
    time.sleep(1.5)
    driver.find_element_by_id("com.lab.testing:id/cb_checkchinese").click()
    driver.find_element_by_id("com.lab.testing:id/btn_save").click()
    driver.find_element_by_name(u"下一步").click()
    driver.find_element_by_name(u"下一步").click()
    driver.find_element_by_name(u"下一步").click()
    driver.find_element_by_name(u"提交").click()

class DpAppTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'#设置平台
        desired_caps['platformVersion'] = '6.0' #系统版本
        desired_caps['deviceName'] = 'emulator-5554'  # 设备id
        #30044ee231868100
        #emulator-5554
        desired_caps['appPackage'] = 'com.lab.testing'  # 包名
        desired_caps['appActivity'] = 'com.lab.testing.ui.LoginActivity'  # 启动的activity
        #com.gt.common.channel.ui.home.views.activity.MainActivity
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    # def tearDown(self):
    #     self.driver.close_app()
    #     self.driver.quit()

    def test_app(self):
        u"""推荐融资"""
        driver = self.driver
        time.sleep(5)
        driver.find_element_by_id("com.lab.testing:id/loginname").clear()
        time.sleep(1)
        driver.find_element_by_id("com.lab.testing:id/loginname").send_keys("13613613677")
        driver.find_element_by_id("com.lab.testing:id/loginnpassword").send_keys("111111")
        driver.find_element_by_name(u"登录").click()

        u'''循环添加行内用户'''
        # n = 2
        # sum = 0
        # counter = 1
        # while counter <= n:
        #     sum = sum + counter
        #     counter += 1
        #     addcheckout(driver)
        for i in range(3):
            addcheckout(driver)
            print u"添加成功"





