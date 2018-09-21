#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import os
browser=webdriver.Chrome()
browser.maximize_window()
browser.get("http://www.qa.egtcp.com")
# 获得当前句柄
nowhandle = browser.current_window_handle
browser.find_element_by_id("username").clear()
size=browser.find_element_by_id("username").size
print size
browser.find_element_by_id("username").send_keys("3588487732@163.com")
bianl=browser.find_element_by_id("password")
bianl.clear()
aaa=bianl.get_attribute('type')
print aaa
bianl.send_keys("a123456")
browser.find_element_by_id("captcha").clear()
browser.find_element_by_id("captcha").send_keys("greattao0818")
browser.find_element_by_class_name("gradient").click()
browser.find_element_by_link_text("管理中心").click()
text=browser.find_element_by_link_text("管理中心").text
print text
shuxz=browser.find_element_by_link_text("管理中心").get_attribute("type")
print shuxz
Sfkj=browser.find_element_by_link_text("管理中心").is_displayed()
print Sfkj
browser.find_element_by_partial_link_text("已上架").click()
browser.find_element_by_id("title").send_keys("a123456")
time.sleep(2)
browser.find_element_by_xpath(".//*[@id='searchtype']/button[1]").click()
wor=browser.find_element_by_id("title")
wor.clear()
wor.send_keys("1efwef")
worr=browser.find_element_by_id("productNo")
worr.send_keys("22223")
time.sleep(1)
#删除最后一位字符
worr.send_keys(Keys.BACK_SPACE)
time.sleep(2)
worr.clear()
time.sleep(1)
worr.send_keys(Keys.SPACE)
worr.send_keys(u"214e124")
time.sleep(1)
#输入框全选
worr.send_keys(Keys.CONTROL,'a')
#键盘回车
worr.send_keys(Keys.ENTER)
#返回当前页面的标题
title=browser.title
print  title

if title==u"产品管理":
    print "title ok!"
else:
    print "title ON！"
#获取当前加载页面的 URL
now_url=browser.current_url
print now_url
if now_url=="http://app.qa.egtcp.com/supplier/shop/product_manage.html":
    print "ok"
else:
    print "ON"

time.sleep(2)
browser.find_element_by_xpath(".//*[@id='post_btn']/tbody/tr[2]/td[2]/div[1]/a/img").click()
#获得所有句柄
allhandles=browser.window_handles
#循环判断窗口是否为当前窗口
for handle in allhandles:
 if handle != nowhandle:
     browser.switch_to_window(handle)
print 'now register window!'
browser.find_element_by_xpath(".//*[@id='quantity']").clear()
browser.find_element_by_xpath(".//*[@id='quantity']").send_keys("1232")
#切换到原先窗口
browser.switch_to_window(nowhandle)
time.sleep(2)
browser.find_element_by_id("title").clear()
browser.find_element_by_id("title").send_keys("555555")

#browser.find_element_by_xpath(".//*[@id='searchtype']/button[1]").click()
#browser.find_element_by_xpath(".//*[@id='post_btn']/tbody/tr[2]/td[2]/div[1]/a/img").click()

