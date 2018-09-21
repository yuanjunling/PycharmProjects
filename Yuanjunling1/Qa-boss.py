#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os,random
browser=webdriver.Chrome()
browser.maximize_window()
browser.get("https://cas.qa.great-tao.com:8443/cas-server/login?service=http://boss.qa.great-tao.com/cas")
nowhandle=browser.current_window_handle
print nowhandle
browser.find_element_by_xpath(".//*[@id='username']").clear()
browser.find_element_by_xpath(".//*[@id='username']").send_keys("hwcrmmanager")
time.sleep(1)
browser.find_element_by_xpath(".//*[@id='password']").clear()
browser.find_element_by_xpath(".//*[@id='password']").send_keys("1234")
browser.find_element_by_xpath(".//*[@id='captcha']").clear()
browser.find_element_by_xpath(".//*[@id='captcha']").send_keys("greattao0818")
browser.find_element_by_xpath(".//*[@id='captcha']").send_keys(Keys.ENTER)
time.sleep(2)
browser.find_element_by_xpath(".//*[@id='menu2']/li[2]/a").click()
title=browser.title
print title
if title=="BOSS":
    print "BOSS ok!"
else:
    print "BOSS NO!"
time.sleep(2)
above=browser.find_element_by_xpath(".//*[@id='menu2']/li[2]/ul/li[1]/a")
#time.sleep(2)
#ActionChains(browser).click_and_hold(above).perform()
time.sleep(2)
browser.find_element_by_link_text("海外_新客户审核").click()
browser.switch_to.default_content()
browser.switch_to.frame(1)
browser.find_element_by_xpath(".//*[@id='pageForm']/div/div/div[1]/div[1]/div/input").send_keys(u"客户名称")
browser.find_element_by_xpath(".//*[@id='pageForm']/div/div/div[1]/div[1]/div/input").send_keys(Keys.ENTER)
browser.find_element_by_xpath(".//*[@id='sample-table-1']/tbody/tr[1]/td[9]/a/i").click()
browser.find_element_by_xpath("html/body/div[1]/div/form/button").click()
time.sleep(2)
# Select(browser.find_element_by_name("status")).select_by_index(1)
status=browser.find_element_by_name("status")
status.click()
ret=Select(status).options
srand =random.Random().choice(ret[1:])
Select(status).select_by_value(srand.get_attribute("value"))