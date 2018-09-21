#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time , os

browser=webdriver.Chrome()
browser.maximize_window()
browser.get("https://cas.qa.great-tao.com:8443/cas-server/login?service=http://boss.qa.great-tao.com/cas")
#获得当前浏览器句柄
nowhandle=browser.current_window_handle
print nowhandle
browser.find_element_by_id("username").clear()
browser.find_element_by_id("username").send_keys("hwcrmmanager")
browser.find_element_by_id("password").clear()
browser.find_element_by_id("password").send_keys("1234")
browser.find_element_by_id("captcha").clear()
browser.find_element_by_id("captcha").send_keys("greattao0818")
browser.find_element_by_id("captcha").send_keys(Keys.ENTER)
browser.implicitly_wait(30)

browser.find_element_by_xpath(".//*[@id='menu2']/li[2]/a").click()
browser.find_element_by_link_text("海外_渠道商分配").click()
browser.switch_to_default_content()
browser.switch_to.frame(1)
browser.find_element_by_xpath(".//*[@id='pageForm']/div/div[1]/div/input").send_keys(u"浙江舟山")
#先定位到下拉框
browser.find_element_by_xpath(".//*[@id='userName_chosen']/a").click()
#再点击下拉框下的选项
browser.find_element_by_xpath(".//*[@id='userName_chosen']/div/ul/li[4]").click()
browser.find_element_by_xpath(".//*[@id='pageForm']/div/div[3]/button").click()
browser.find_element_by_xpath(".//*[@id='main-container']/div/div/div[2]/div[2]/div/div[1]/button").click()
title=browser.title
print title
#获取弹出窗口id
browser.switch_to_frame("layui-layer-iframe1")
browser.find_element_by_id("enterpriseName").send_keys(u"我是红色字体")
time.sleep(3)
browser.find_element_by_id("searchService").click()
#先定位到下拉框
browser.find_element_by_xpath(".//*[@id='userName_chosen']/a").click()
#再点击下拉框下的选项
browser.find_element_by_xpath(".//*[@id='userName_chosen']/div/ul/li[3]").click()
#browser.find_element_by_id("jqg_grid-table_104").click()
#browser.find_element_by_xpath(".//*[@id='pageForm']/div[2]/div/div[3]/button").click()
time.sleep(2)
js="var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)