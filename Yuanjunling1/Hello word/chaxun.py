#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re ,random,os
import HTMLTestRunner

browser=webdriver.Chrome()
browser.maximize_window()
browser.get("https://cas.qa.great-tao.com:8443/cas-server/login?service=http://boss.qa.great-tao.com/cas")
browser.implicitly_wait(30)
browser.find_element_by_id("username").send_keys("dingni")
browser.find_element_by_id("password").send_keys("1234")
browser.find_element_by_id("captcha").send_keys("greattao0818")
browser.find_element_by_id("captcha").send_keys(Keys.ENTER)
time.sleep(2)
browser.find_element_by_link_text(u"信用查询").click()
time.sleep(2)
browser.find_element_by_link_text(u"违约查询管理").click()
time.sleep(2)
browser.find_element_by_link_text(u"违约查询申请").click()
time.sleep(3)
browser.switch_to.default_content()
browser.switch_to.frame(1)
time.sleep(3)

Select(browser.find_element_by_id("status")).select_by_index(1)
time.sleep(2)
browser.find_element_by_id("applySearch").click()
time.sleep(2)
browser.find_element_by_xpath(".//*[@id='applyInfosTable']/tbody/tr[1]/td[11]/a[2]").click()
time.sleep(2)
browser.find_element_by_id("modify_sure").click()