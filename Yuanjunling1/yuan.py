#coding=utf-8
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("http://qa.egtcp.com")
print "设置浏览器长宽"
browser.set_window_size(600,800)
browser.quit()