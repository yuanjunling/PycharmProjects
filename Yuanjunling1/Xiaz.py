# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from time import sleep

options = webdriver.ChromeOptions()
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': 'd:\\'}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(executable_path='C:\Python27\\chromedriver.exe', chrome_options=options)
driver.get('http://sahitest.com/demo/saveAs.htm')
driver.find_element_by_xpath('html/body/a[1]').click()
sleep(3)
driver.quit()