# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Ojo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://cas.qa.great-tao.com:8443/cas-server/login?service=http://boss.qa.great-tao.com/cas"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ojo(self):
        driver = self.driver
        driver.get(self.base_url + "/cas-server/login?service=http://boss.qa.great-tao.com/cas")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("yuanjunling")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("1234")
        driver.find_element_by_id("captcha").clear()
        driver.find_element_by_id("captcha").send_keys("greattao0818")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text(u"BOSS系统").click()
        driver.find_element_by_link_text(u"销售线索").click()
        driver.find_element_by_link_text(u"添加线索").click()
        Select(driver.find_element_by_id("type")).select_by_visible_text(u"采购线索")
        Select(driver.find_element_by_id("source")).select_by_visible_text(u"互联网（线上运营）")
        driver.find_element_by_id("sourceRemark").clear()
        driver.find_element_by_id("sourceRemark").send_keys("sd fsdf sdf")
        Select(driver.find_element_by_id("roleBack")).select_by_visible_text(u"采购商")
        driver.find_element_by_id("company").clear()
        driver.find_element_by_id("company").send_keys("ddddddd")
        driver.find_element_by_id("contact").clear()
        driver.find_element_by_id("contact").send_keys("dddd")
        driver.find_element_by_id("position").clear()
        driver.find_element_by_id("position").send_keys("ddddd")
        driver.find_element_by_id("tel").clear()
        driver.find_element_by_id("tel").send_keys("fffff")
        driver.find_element_by_id("other").clear()
        driver.find_element_by_id("other").send_keys("yuannnn")
        driver.find_element_by_id("content").clear()
        driver.find_element_by_id("content").send_keys("beizhu")
        driver.find_element_by_id("btn-addAttach").click()
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        driver.find_element_by_id("submit").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
