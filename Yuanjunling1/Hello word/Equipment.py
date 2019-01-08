#coding=utf-8
from selenium import webdriver
from random import choice
import time,unittest,random,HTMLParser,hashlib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

def adduser(driver):
    driver.switch_to.default_content()
    driver.switch_to_frame(1)
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='addUser']/span/span[1]").click()
    time.sleep(2)
    driver.switch_to_frame("paramIframe")
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='paramForm']/div[1]/span/input[1]").send_keys(
        u"test%d" % random.randrange(1, 9999, ))
    time.sleep(0.5)
    driver.find_element_by_xpath(".//*[@id='paramForm']/div[2]/span/input[1]").send_keys(
        random.choice(['139', '188', '185', '136', '158', '151']) + "".join(
            random.choice("0123456789") for i in range(8)))
    time.sleep(0.5)
    driver.find_element_by_xpath(".//*[@id='paramForm']/div[3]/span/input[1]").send_keys(
        random.choice(['139', '188', '185', '136', '158', '151']) + "".join(
            random.choice("0123456789") for i in range(8)) + "@qq.com")
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='orgIdDiv']/span/span/a").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[starts-with(@id,'_easyui_tree_')]").click()
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='paramForm']/div[5]/span/span/a").click()
    time.sleep(2)
    driver.find_element_by_xpath("html/body/div[5]/div/ul/li[1]/div[1]/span[4]").click()
    time.sleep(2)
    driver.find_element_by_xpath(".//*[@id='paramForm']/div[7]/span/span/a").click()
    time.sleep(2)
    driver.find_element_by_xpath("html/body/div[2]/div/div[2]").click()
    time.sleep(2)
    driver.find_element_by_xpath("html/body/div[1]/div[2]/div[1]/a[2]/span/span[1]").click()
    time.sleep(2)
    driver.switch_to.default_content()
    driver.switch_to_frame(1)
    time.sleep(2)
    driver.find_element_by_xpath("html/body/div[17]/div[3]/a/span/span").click()

    return


class Boss(unittest.TestCase):
    def setUp(self):
        u"""设备报修系统"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.Boss_url = "http://47.105.192.106:8080/RepairServiceManage_mvn-0.0.1-SNAPSHOT/"
        self.verificationErrors=[]
        self.accept_next_alet=True

    def test_login(self):
        driver = self.driver
        driver.get(self.Boss_url)
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath(".//*[@id='loginForm']/div[3]/span/input[1]").send_keys("admin")
        driver.find_element_by_xpath(".//*[@id='loginForm']/div[4]/span/input[1]").send_keys("123456")
        driver.find_element_by_xpath(".//*[@id='loginForm']/div[4]/span/input[1]").send_keys(Keys.ENTER)


        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='A']/span/span[1]").click()
        time.sleep(0.5)
        driver.find_element_by_xpath(".//*[@id='AAB0000']/span/span[1]").click()
        time.sleep(2)

        n = 5
        sum = 0
        counter = 1

        while counter <= n:
            sum = sum + counter
            counter += 1
            adduser(driver)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

if __name__ == "__main__":
    unittest.main()
    runner = HTMLTestRunner.HTMLTestRunner(

        stream=fp,
        title=u"渠道助手测试报告",
        description=u"用例执行情况："
    )



































