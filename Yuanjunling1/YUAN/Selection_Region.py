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
import unittest, time, re ,random,os,sys,xlrd, HTMLTestRunner


def Selection_Region(driver):
    status = driver.find_element_by_id("district")
    status.click()
    ret = Select(status).options
    srand = random.Random().choice(ret[1:])
    Select(status).select_by_value(srand.get_attribute("value"))
