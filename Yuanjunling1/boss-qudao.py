#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time,login

browser=webdriver.Chrome()
browser.get("https://cas.qa.great-tao.com:8443/cas-server/login?service=http://boss.qa.great-tao.com/cas")
browser.implicitly_wait(30)
login.login(browser)

