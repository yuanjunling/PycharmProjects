#coding=utf-8
from selenium import webdriver
from random import choice
import time,unittest,random,HTMLParser,hashlib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class LIB(unittest.TestCase):
    def setUp(self):
        u"""登录"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.Boss_url = "http://192.168.0.254:8080/inspectpass_platform/login.jsp"
        self.verificationErrors = []
        self.accept_next_alet = True
    def test_login(self):
        driver = self.driver
        driver.get(self.Boss_url)
        driver.maximize_window()
        driver.implicitly_wait(30)
        u'''登录系统'''
        driver.find_element_by_id("loginName").send_keys("admin")
        driver.find_element_by_id("loginPwd").send_keys("123456")
        driver.find_element_by_id("loginPwd").send_keys(Keys.ENTER)
        time.sleep(1)
        u"""业务管理"""
        driver.find_element_by_xpath("html/body/div[1]").click()
        driver.find_element_by_xpath(".//*[@id='nav']/li[1]/a/cite").click()
        time.sleep(0.5)
        driver.find_element_by_xpath(".//*[@id='nav']/li[1]/ul/li[2]/a/cite").click()



