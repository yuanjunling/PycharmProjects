#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import by
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
class Baidu(unittest.TestSuite):#Baidu 类继承 unittest.TestCase 类，从 TestCase 类继承是告诉 unittest 模块的方式
    def setUP(self):#setUp 用于设置初始化的部分，在测试用例执行前，这个方法中的函数将先被调用。这里将浏览器的调用和 URL 的访问放到初始化部分
        self.driver=webdriver.Chrome()
        self.driver_url=("http://www.baidu.com")
        self.verificationErrors = [] #脚本运行时，错误的信息将被打印到这个列表中。
        self.accept_next_alert = True #是否继续接受下一个警告

    def test_baidu(self):#
        driver = self.driver
        driver.get(self.driver_url+"/")
        driver.find_element_by_id("kw").send_keys("selenium webdriver")
        driver.find_element_by_id("su").click()
    def is_element_present(self,how,what):#对弹窗异常的处理
        try:self.driver.find_element(by=how,value=what)
        except NoSuchElementException,e:return False
        return True










