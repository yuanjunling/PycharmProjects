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
import unittest, time, re ,random,os,sys,xlrd, HTMLTestRunner,log

class Boss1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.Boss_url = "http://boss.qa.great-tao.com/"
        self.verificationErrors = []
        self.accept_next_alet = True
    def test_Guonei(self):
        u"""创建国内渠道"""
        driver = self.driver
        driver.get(self.Boss_url)
        driver.maximize_window()
        driver.implicitly_wait(30)
        #登录Boss系统

