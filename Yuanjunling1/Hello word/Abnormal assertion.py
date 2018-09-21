#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re ,random,os
import HTMLTestRunner
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# import  time, re,HTMLTestRunner
# import unittest
# browser=webdriver.Chrome()
# browser.get("http://www.baidu.com")
# try:
#     browser.find_element_by_id("kwssss").send_keys("aaaaaaa")
#     browser.find_element_by_id("su").click()
# except:
#     browser.get_screenshot_as_file(u"E:\工作任务\error_png.png")

class Boss(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.Boss_url = "https://cas.qa.great-tao.com:8443/cas-server/login?service=http://boss.qa.great-tao.com/cas"
        self.verificationErrors = []
        self.accept_next_alet=True

    def test_boss(self):
        try:
            driver = self.driver
            driver.get(self.Boss_url)
            driver.maximize_window()
            driver.find_element_by_id("username").send_keys("yuanjunling")
            driver.find_element_by_id("password").send_keys("1234")
            driver.find_element_by_id("captcha").send_keys("greattao0818")
            driver.find_element_by_id("captcha").send_keys(Keys.ENTER)
            driver.close()

        except:
            driver.get_screenshot_as_file(u"E:\工作任务\异常截图\error_png.png")
        def is_element_present(self,how,what):
         try:
             self.driver.find_element(by=how,value=what)
         except NoSuchElementException,e :return  False
         return True
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
# if __name__ == "__main__ ":
# 定义一个单元测试容器
    # testunit = unittest.TestSuite()
# 将测试用例加入到测试容器中
    # testunit.addTest(Boss("test_boss"))
# 定义个报告存放路径，支持相对路径
    # filename = 'D:\\selenium_python\\report\\result.html'
    # fp =  file(filename, 'wb')
    # 定义测试报告
    # runner = HTMLTestRunner.HTMLTestRunner(
    #     stream=fp,
    #     title=u'BOSS报告',
    #     description=u'用例执行情况：')
    # 运行测试用例
    # runner.run(testunit)

