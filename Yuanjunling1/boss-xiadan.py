# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os

class BossXiadan(unittest.TestCase):
    def setUp(self):
        chrome_driver=os.path.abspath(r'C:\Python27\chromedriver.exe')
        os.environ['webdriver.chrome.driver']=chrome_driver
        self.driver=webdriver.Chrome()
        self.driver.get("https://cas.qa.great-tao.com:8443/cas-server/login?service=http://boss.qa.great-tao.com/cas")
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_boss_xiadan(self):
        driver = self.driver
        driver.get("https://cas.qa.great-tao.com:8443/cas-server/login?service=http://boss.qa.great-tao.com/cas")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("dingni")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("1234")
        driver.find_element_by_id("captcha").clear()
        driver.find_element_by_id("captcha").send_keys("greattao0818")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text(u"BOSS系统").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"销售线索").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"添加线索").click()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'http://boss.qa.great-tao.com/boss-leads-web/leads/add')]"))
        #切换frame
        driver.find_element_by_id("sourceRemark").clear()
        driver.find_element_by_id("sourceRemark").send_keys("test")
        driver.find_element_by_id("company").clear()
        driver.find_element_by_id("company").send_keys("dntest")
        xiansuo_style1=driver.find_element_by_id("type")
        Select(xiansuo_style1).select_by_value('3')#下拉框选择
        xiansuo_source=driver.find_element_by_id("source")
        Select(xiansuo_source).select_by_value('3')
        driver.find_element_by_id("contact").clear()
        driver.find_element_by_id("contact").send_keys("dn")
        driver.find_element_by_id("tel").clear()
        driver.find_element_by_id("tel").send_keys("15987598758")
        driver.find_element_by_id("email").clear()
        driver.find_element_by_id("email").send_keys("156848@126.com")
        driver.find_element_by_id("content").clear()
        driver.find_element_by_id("content").send_keys("dntest")
        driver.find_element_by_id("submit").click()
        driver.switch_to.default_content()#换回主frame
        driver.find_element_by_link_text(u"线索分配").click()
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'http://boss.qa.great-tao.com/boss-leads-web/leads/director/list')]"))
        #切换frame
        xiansuo_style2=driver.find_element_by_id("type")
        Select(xiansuo_style2).select_by_value('3')
        xiansuo_status2=driver.find_element_by_id("status")
        Select(xiansuo_status2).select_by_value('1')
        driver.find_element_by_id("btn_query").click()
        driver.maximize_window()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='table']/tbody/tr[1]/td[10]/a[2]").click()
        time.sleep(2)
        driver.switch_to.frame(driver.find_element_by_id("layui-layer-iframe1"))#切换frame
        div_fenpei=driver.find_element_by_class_name("col-xs-6").find_element_by_id("receiver")
        Select(div_fenpei).select_by_value('53')
        driver.find_element_by_id("confirm").click()
        driver.switch_to.default_content()#换回主frame
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'http://boss.qa.great-tao.com/boss-leads-web/leads/director/list')]"))
        Select(xiansuo_status2).select_by_value('7')
        time.sleep(1)
        driver.find_element_by_id("btn_query").click()
        time.sleep(3)
        driver.find_element_by_xpath("//*[@id='table']/tbody/tr[1]/td[10]/a[1]").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"关联").click()
        time.sleep(3)
        driver.switch_to.frame(driver.find_element_by_id("layui-layer-iframe1"))#切换frame
        driver.find_element_by_xpath("//*[@id='table']/tbody/tr[1]").click()
        driver.find_element_by_id("confirm").click()
        driver.switch_to.default_content()#换回主frame
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'http://boss.qa.great-tao.com/boss-leads-web/leads/director/list')]"))
        driver.find_element_by_link_text(u"跟进").click()
        time.sleep(1)
        driver.switch_to.default_content()#换回主frame
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'http://boss.qa.great-tao.com/boss-leads-web/leads/director/list')]"))
        driver.switch_to.frame(driver.find_element_by_id("layui-layer-iframe1"))#切换frame
        time.sleep(1)
        driver.find_element_by_id("followupRemark").clear()
        driver.find_element_by_id("followupRemark").send_keys("test dn")
        driver.find_element_by_id("followupDate").click()
        driver.find_element_by_xpath("/html/body/div[2]/div[3]/table/tbody/tr[4]/td[3]").click()
        driver.find_element_by_id("confirm").click()
        driver.switch_to.default_content()#换回主frame
        driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'http://boss.qa.great-tao.com/boss-leads-web/leads/director/list')]"))
        driver.find_element_by_link_text(u"下单").click()
        driver.find_element_by_id("selectServiceProvider").click()
        driver.find_element_by_id("popup").click()
        driver.find_element_by_xpath("(//input[@name='btSelectItem'])[35]").click()
        driver.find_element_by_id("queryService").click()
        driver.find_element_by_name("orderAddressList[0].name").clear()
        driver.find_element_by_name("orderAddressList[0].name").send_keys("testdn001")
        driver.find_element_by_name("orderAddressList[0].address").clear()
        driver.find_element_by_name("orderAddressList[0].address").send_keys("testdn001")
        driver.find_element_by_name("orderAddressList[1].name").clear()
        driver.find_element_by_name("orderAddressList[1].name").send_keys("testdn0001")
        driver.find_element_by_name("orderAddressList[2].name").clear()
        driver.find_element_by_name("orderAddressList[2].name").send_keys("testdn00001")
        driver.find_element_by_name("goodsList[0].goodsName").clear()
        driver.find_element_by_name("goodsList[0].goodsName").send_keys("testdn0001")
        driver.find_element_by_name("goodsList[0].num").clear()
        driver.find_element_by_name("goodsList[0].num").send_keys("1")
        Select(driver.find_element_by_name("goodsList[0].unit")).select_by_visible_text("CTNS")
        driver.find_element_by_name("goodsList[0].grossWeight").clear()
        driver.find_element_by_name("goodsList[0].grossWeight").send_keys("1")
        driver.find_element_by_name("goodsList[0].measurement").clear()
        driver.find_element_by_name("goodsList[0].measurement").send_keys("1")
        driver.find_element_by_xpath("(//input[@name='orderExpand.containerMark'])[2]").click()
        driver.find_element_by_xpath("//div[@id='sizzle-1489114881098']/div[3]/table/tbody/tr/td[5]").click()
        driver.find_element_by_xpath("//div[@id='sizzle-1489114881098']/div[3]/table/tbody/tr[3]/td[6]").click()
        driver.find_element_by_id("select2-orderportOfShipment-qa-container").click()
        driver.find_element_by_css_selector("span.select2-selection__placeholder").click()
        Select(driver.find_element_by_name("orderExpand.typeOfShipping")).select_by_visible_text(u"海运")
        Select(driver.find_element_by_name("order.freightPayableat")).select_by_visible_text(u"运费预付")
        driver.find_element_by_name("selectService").click()
        driver.find_element_by_name("orderExpand.entrustName").clear()
        driver.find_element_by_name("orderExpand.entrustName").send_keys("11")
        driver.find_element_by_name("orderExpand.entrustTel").clear()
        driver.find_element_by_name("orderExpand.entrustTel").send_keys("11")
        Select(driver.find_element_by_id("haha")).select_by_visible_text(u"海运费")
        driver.find_element_by_name("logisticsCosts[3].price").clear()
        driver.find_element_by_name("logisticsCosts[3].price").send_keys("11")
        Select(driver.find_element_by_id("store-name")).select_by_visible_text(u"吊机费")
        driver.find_element_by_name("logisticsCosts[4].price").clear()
        driver.find_element_by_name("logisticsCosts[4].price").send_keys("11")
        driver.find_element_by_name("logisticsCosts[1].price").clear()
        driver.find_element_by_name("logisticsCosts[1].price").send_keys("11")
        driver.find_element_by_id("saveService").click()
   
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
    
    '''def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)'''

if __name__ == "__main__":
    unittest.main()
