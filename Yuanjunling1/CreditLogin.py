#!-*- coding:utf-8  -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest,time


class CreditLogin(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.home_url='https://cas.qa.great-tao.com:8443/cas-server/login?service=http://boss.qa.great-tao.com/cas'
        self.boss_index_url='http://boss.qa.great-tao.com/index'
        #脚本运行时，错误的信息将打印到这个列表中
        self.verificationErrors=[]
        #是否接受下一个A警告
        self.accept_next_alert=True

    def testDefaultInquiry(self):
        '''BOSS后台 违约查询申请测试'''
        driver=self.driver
        driver.get(self.home_url)
        print "Now access %s" % (self.home_url)
        # 输入用户名
        driver.find_element_by_name("username").send_keys('dingni')
        print "Insert username success"
        # 输入密码
        driver.find_element_by_name("password").send_keys('1234')
        print "Insert password success"
        # 输入验证码
        driver.find_element_by_name("captcha").send_keys('greattao0818')
        print "Insert captcha success"
        # 提交
        driver.find_element_by_name("submit").click()
        print "Login success!"
        #点击菜单加载列表
        driver.find_element_by_link_text(u"信用查询").click()
        driver.find_element_by_link_text(u"违约查询管理").click()
        driver.find_element_by_link_text(u"违约查询申请").click()
        # 查询“未处理”订单
        try:
            #先跳转到iframe框架,然后搜索匹配的结果
            elementi=driver.find_element_by_xpath("//*[@id='iframe_box']/div[2]/iframe")
            driver.switch_to_frame(elementi)

            driver.find_element_by_id("applicantEmail").send_keys("panshuyuan@qq.com")
            s1 = Select(driver.find_element_by_id("status"))
            s1.select_by_value("0")
            driver.find_element_by_id("applySearch").click()
            print "LoadOrders success"

            '''
            wait = WebDriverWait(driver, 10)
            #wait.until(lambda driver: driver.find_element_by_id("applicantEmail"))

            applicantEmail = wait.until(EC.presence_of_element_located(By.ID, "applicantEmail"))
            applicantEmail.clear()
            applicantEmail.send_keys("panshuyuan@qq.com")

            applySearch = wait.until(EC.visibility_of_element_located(By.ID, "applySearch"))
            applySearch.click()
            print "LoadOrders success"
             '''

        except AssertionError as e:
            print e

        #点击“处理”
        # 先跳转到iframe框架,然后搜索匹配的结果
        elementi1 = driver.find_element_by_xpath("//*[@id='iframe_box']/div[2]/iframe")
        driver.switch_to_frame(elementi1)
        driver.find_element_by_class_name("handle").click()
        driver.find_element_by_id("sendEmail_radio").click()
        driver.find_element_by_xpath("//*[@id='model1']/div[1]/div/input").send_keys("Apple")
        driver.find_element_by_id("emailSearch").click()


    def tearDown(self):
        driver=self.driver
        driver.close()
        self.assertEqual([],self.verificationErrors)