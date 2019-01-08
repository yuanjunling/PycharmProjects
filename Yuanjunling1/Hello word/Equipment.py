#coding=utf-8
from selenium import webdriver
from random import choice
import time,unittest,random,HTMLParser,hashlib
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class Boss(unittest.TestCase):
    def setUp(self):
        u"""设备报修系统"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.Boss_url = "https://repair.nbeasy.net.cn:4434/RepairServiceManageNbzh2/"
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

        print nowhandle
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='A']/span/span[1]").click()
        time.sleep(0.5)
        driver.find_element_by_xpath(".//*[@id='AAB0000']/span/span[1]").click()
        time.sleep(2)
        driver.switch_to.default_content()
        driver.switch_to_frame(1)
        driver.find_element_by_xpath(".//*[@id='addUser']/span/span[1]").click()
        time.sleep(2)
        driver.switch_to_frame("paramIframe")
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='paramForm']/div[1]/span/input[1]").send_keys(u"test%d"%random.randrange(1, 9999,))
        time.sleep(0.5)
        driver.find_element_by_xpath(".//*[@id='paramForm']/div[2]/span/input[1]").send_keys(random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8)))
        time.sleep(0.5)
        driver.find_element_by_xpath(".//*[@id='paramForm']/div[3]/span/input[1]").send_keys(random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))+"@qq.com")
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='orgIdDiv']/span/span/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='_easyui_tree_1']/span[2]").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='paramForm']/div[5]/span/span/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='_easyui_tree_173']/span[1]").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='_easyui_tree_174']/span[4]").click()
        # status1 = driver.find_element_by_xpath(".//*[@id='paramForm']/div[7]/span/span/a")
        # status1.click()
        # ret = Select(status1).options
        # srand = random.Random().choice(ret[1:])
        # Select(status1).select_by_index(srand.get_attribute(1))
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='paramForm']/div[7]/span/span/a").click()
        time.sleep(2)
        driver.find_element_by_id("_easyui_combobox_i4_1").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[1]/a[2]/span/span[1]").click()
























