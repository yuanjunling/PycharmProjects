# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Testxiaos(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://cas.qa.great-tao.com:8443/cas-server/login?service=http://boss.qa.great-tao.com/cas"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_xiaos(self):
        driver = self.driver
        driver.get(self.base_url + "/index#http://boss.qa.great-tao.com/boss-leads-web/leads/add")
        driver.find_element_by_xpath("//form[@id='form']/div[3]/div/button").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=layui-layer-iframe1 | ]]
        driver.find_element_by_id("name").clear()
        driver.find_element_by_id("name").send_keys(u"原浆酒")
        driver.find_element_by_id("discription").clear()
        driver.find_element_by_id("discription").send_keys(u"么么么么")
        driver.find_element_by_id("specification").clear()
        driver.find_element_by_id("specification").send_keys(u"钢铁")
        driver.find_element_by_id("purNumber").clear()
        driver.find_element_by_id("purNumber").send_keys("222")
        driver.find_element_by_id("argument").clear()
        driver.find_element_by_id("argument").send_keys("5555555")
        driver.find_element_by_id("purpose").clear()
        driver.find_element_by_id("purpose").send_keys("2222")
        driver.find_element_by_id("targetPrice").clear()
        driver.find_element_by_id("targetPrice").send_keys("222222")
        driver.find_element_by_css_selector("div.datetimepicker-days > table..table-condensed > tfoot > tr > th.today").click()
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
