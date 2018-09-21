#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep
from random import choice
import unittest, time, re ,random,os,sys,xlrd, HTMLTestRunner,login

class CRM(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.Boss_url = "http://boss.qa.great-tao.com/"
        self.verificationErrors = []
        self.accept_next_alet = True
    def test_crm(self):
        u"""国内CRM"""
        driver = self.driver
        driver.get(self.Boss_url)
        driver.maximize_window()
        driver.implicitly_wait(30)
        # 登录BOSS系统
        login.login(driver)
        nowhandle = driver.current_window_handle
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='Hui-nav']/ul/li[4]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='menu2']/li[1]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='menu2']/li[1]/ul/li[3]/a").click()
        time.sleep(2)
        # 从frame中切回主文档
        driver.switch_to.default_content()
        driver.switch_to_frame(1)

        table = driver.find_element_by_id('sample-table-1')
        table_rows = table.find_elements_by_tag_name('tr')
        print "总行数:", len(table_rows)
        row1_col2 = table_rows[1].find_elements_by_tag_name('td')[0].text
        print "第一行第二列的text:", row1_col2

