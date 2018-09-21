#coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time , os
Bianl=webdriver.Chrome()
Bianl.get("https://cas.qa.great-tao.com:8443/cas-server/login?service=http://boss.qa.great-tao.com/cas")
Bianl.add_cookie({'name':'Login_UserNumber', 'value':'hwcrmmanager'})
Bianl.add_cookie({'name':'Login_Passwd', 'value':'1234'})
#再次访问 xxxx 网站，将会自动登录
Bianl.get("https://cas.qa.great-tao.com:8443/cas-server/login?service=http://boss.qa.great-tao.com/cas")
time.sleep(3)

title=Bianl.title
print title