# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re,login

class Yuanjuntest01(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.xiaosxx_url = 'https://cas.qa.great-tao.com:8443/cas-server/login?service=http://boss.qa.great-tao.com/cas'
        self.verificationErrors = []
        self.accept_next_alet = True
    
    def test_yuanjuntest01(self):
        driver = self.driver
        driver.get(self.xiaosxx_url)
        login.login(driver)
        time.sleep(2)
        driver.find_element_by_link_text(u"BOSS系统").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"销售线索").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"添加线索").click()
        time.sleep(2)
        Select(driver.find_element_by_id("type")).select_by_visible_text(u"采购线索")
        time.sleep(2)
        Select(driver.find_element_by_id("source")).select_by_visible_text(u"互联网（线上运营）")
        time.sleep(2)
        driver.find_element_by_id("sourceRemark").clear()
        time.sleep(2)
        driver.find_element_by_id("sourceRemark").send_keys(u"水电费水电费")
        time.sleep(2)
        Select(driver.find_element_by_id("roleBack")).select_by_visible_text(u"采购商")
        time.sleep(2)
        driver.find_element_by_id("company").clear()
        time.sleep(2)
        driver.find_element_by_id("company").send_keys(u"水电费水电费水电费")
        time.sleep(2)
        driver.find_element_by_id("contact").clear()
        time.sleep(2)
        driver.find_element_by_id("contact").send_keys(u"水电费水电费第三方")
        time.sleep(2)
        driver.find_element_by_id("position").clear()
        time.sleep(2)
        driver.find_element_by_id("position").send_keys(u"水电费第三方水电费")
        time.sleep(2)
        driver.find_element_by_id("tel").clear()
        time.sleep(2)
        driver.find_element_by_id("tel").send_keys(u"水电费水电费水电费")
        time.sleep(2)
        driver.find_element_by_id("other").clear()
        time.sleep(2)
        driver.find_element_by_id("other").send_keys(u"水电费水电费水电费")
        time.sleep(2)
        driver.find_element_by_id("content").clear()
        time.sleep(2)
        driver.find_element_by_id("content").send_keys(u"水电费水电费水电费水电费水电费")
        time.sleep(2)
        driver.find_element_by_id("btn-addAttach").click()
        time.sleep(2)
        # ERROR: Caught exception [Error: locator strategy either id or name must be specified explicitly.]
        driver.find_element_by_id("submit").click()
        time.sleep(2)
        driver.find_element_by_xpath("//form[@id='form']/div[3]/div/button").click()
        time.sleep(2)
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=layui-layer-iframe1 | ]]
        driver.find_element_by_id("name").clear()
        time.sleep(2)
        driver.find_element_by_id("name").send_keys(u"水电费水电费水电费")
        time.sleep(2)
        driver.find_element_by_id("discription").clear()
        time.sleep(2)
        driver.find_element_by_id("discription").send_keys(u"第三方水电费水电费")
        time.sleep(2)
        driver.find_element_by_id("specification").clear()
        time.sleep(2)
        driver.find_element_by_id("specification").send_keys(u"第三方水电费水电费")
        time.sleep(2)
        driver.find_element_by_id("purNumber").clear()
        time.sleep(2)
        driver.find_element_by_id("purNumber").send_keys("32323232")
        time.sleep(2)
        driver.find_element_by_id("argument").clear()
        time.sleep(2)
        driver.find_element_by_id("argument").send_keys("32233232")
        time.sleep(2)
        driver.find_element_by_id("purpose").clear()
        time.sleep(2)
        driver.find_element_by_id("purpose").send_keys("32323232")
        time.sleep(2)
        driver.find_element_by_id("targetPrice").clear()
        time.sleep(2)
        driver.find_element_by_id("targetPrice").send_keys("32323232")
        time.sleep(2)
        driver.find_element_by_css_selector("div.datetimepicker-days > table..table-condensed > tfoot > tr > th.today").click()
        time.sleep(2)
        driver.find_element_by_id("submit").click()
        time.sleep(2)
    
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
