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
import unittest, time, re ,random,os,sys,xlrd, HTMLTestRunner,login
class guonwai(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.BOSS_url = "https://cas.qa.great-tao.com:8443/cas-server/login?service=http://boss.qa.great-tao.com/cas"
        self.verificationErrors=[]
        self.accept_next_alet=True
    def test_guowai(self):
        u"""创建国外渠道"""
        driver=self.driver
        driver.get(self.BOSS_url)
        driver.maximize_window()
        driver.implicitly_wait(30)
        #登录BOSS系统
        login.login(driver)
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='Hui-nav']/ul/li[2]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='menu2']/li[12]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='menu2']/li[12]/ul/li[1]/a").click()
        # 从frame中切回主文档
        driver.switch_to.default_content()
        driver.switch_to_frame(1)
        # 创建国内渠道
        try:
            driver.find_element_by_xpath("html/body/div[1]/div[1]/div/div[1]/div/a").click()
            driver.find_element_by_xpath(".//*[@id='foreignChannel']/input").click()

            driver.find_element_by_id("agent").send_keys(random.choice( ['apple', 'pear', 'peach', 'orange', 'lemon']))
            driver.find_element_by_id("legalPerson").send_keys(random.choice(['sdfdsfds','jkhfgdk','dsfsdfsdf','dsfdsfdsf']))
            driver.find_element_by_id("tel").send_keys(random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8)))
            driver.find_element_by_id("email").send_keys("261412489@qq.com")
            driver.find_element_by_id("margin").send_keys(random.randrange(1,99999))
            driver.find_element_by_id("initialFee").send_keys(random.randrange(1,99999))
            driver.find_element_by_id("beginTime").click()
            driver.find_element_by_xpath("html/body/div[2]/div[3]/table/tfoot/tr/th").click()
            driver.find_element_by_id("timeLimit").send_keys(random.randrange(1,99))
            driver.find_element_by_class_name("webuploader-element-invisible").send_keys("E:\ipg\popoo.jpeg")
            time.sleep(2)
            qudao = u"渠道名称%d" % random.randrange(1, 9999, )
            driver.find_element_by_id("name").send_keys(qudao)
            Select(driver.find_element_by_id("managerId")).select_by_index(4)
            #, 'mid', 'pri'
            random1 = random.choice(['adv','mid', 'pri'])
            driver.find_element_by_id(random1).click()
            if  random1=='adv':
                driver.find_element_by_xpath("username").send_keys(u"高级渠道账号%d"%random.randrange(1, 9999, ))
                time.sleep(2)
                # Select(driver.find_element_by_id("span-country")).select_by_index(2)
                driver.find_element_by_name(u"渠道独家代理区域：").click()


                driver.find_element_by_xpath(".//*[@id='countrys_chosen']/div/ul/li[9]").click()

                driver.find_element_by_id("btn-add-country").click()

            elif random1=='mid':
                driver.find_element_by_id("username").send_keys(u"中级渠道账号%d" % random.randrange(1, 9999, ))
                # Select(driver.find_element_by_xpath(".//*[@id='countrys_chosen']/a/span")).select_by_value("KL")
                time.sleep(2)
                driver.find_element_by_class_name("chosen-single").click()
                time.sleep(2)
                driver.find_element_by_xpath(".//*[@id='countrys_chosen']/div/ul/li[9]").click()
                time.sleep(2)
                driver.find_element_by_id("btn-add-country").click()

            else:

                driver.find_element_by_id("username").send_keys(u"低级渠道账号%d" % random.randrange(1, 9999, ))


            driver.find_element_by_id("btn-submit").click()





        except:
            now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
            driver.get_screenshot_as_file(u"E:\\工作任务\异常截图\\" + now + "error_png.png")