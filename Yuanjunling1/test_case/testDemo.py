#  -*- coding:utf-8 -*-

import os
import unittest
from appium import webdriver
from time import sleep
from random import choice
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time,random,HTMLTestRunner

# Appium配置
# PATH = lambda p: os.path.abspath(
#     os.path.join(os.path.dirname(__file__),p)
#
# )
class DpAppTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'#设置平台
        desired_caps['platformVersion'] = '6.0' #系统版本
        desired_caps['deviceName'] = 'emulator-5554'  # 设备id
        #30044ee231868100
        #emulator-5554
        desired_caps['appPackage'] = 'com.gt.common.channel'  # 包名
        desired_caps['appActivity'] = 'com.gt.common.channel.ui.gui.views.WelcomeActivity'  # 启动的activity
        #com.gt.common.channel.ui.home.views.activity.MainActivity
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)




# earDown 方法在每个测试方法执行后调用，这个地方做所有清理工作，如退出
    def tearDown(self):
        self.driver.close_app()
        self.driver.quit()



    def test_app(self):
        u"""推荐融资"""
        driver = self.driver
        time.sleep(5)
        #点击我的客户列表
        driver.find_element_by_name(u"我的联系人").click()
        time.sleep(3)
        #选中联系人左滑
        driver.swipe(147,807,21,781,1000)
        time.sleep(1)
        #点击融资推荐按钮
        print type(driver.find_element_by_id("com.gt.common.channel:id/finance_iv"))

        driver.find_element_by_id("com.gt.common.channel:id/finance_iv").click()
        #点击融资推荐+按钮
        time.sleep(1)
        driver.find_element_by_id("com.gt.common.channel:id/id_action_new").click()
        driver.implicitly_wait(30)
        #填写融资资料——申请表

        time.sleep(5)
        #driver.find_element_by_id("com.gt.common.channel:id/company_name_til").send_keys(u"浙江舟山供应商%d"%random.randrange(1, 9999))
        # driver.find_element_by_android_uiautomator('new UiSelector().text("公司名称")').send_keys(u"回复后返回回复回复111")
        driver.find_element_by_id("com.gt.common.channel:id/goods_til").send_keys(u"飞机大炮火箭筒11")
        driver.find_element_by_id("com.gt.common.channel:id/purchase_til").send_keys('134234234')
        driver.find_element_by_id("com.gt.common.channel:id/legal_person_til").send_keys(u"胡彪11")
        driver.find_element_by_id("com.gt.common.channel:id/contact_rl").click()
        driver.find_element_by_id("com.gt.common.channel:id/name_tv").click()
        driver.find_element_by_id("com.gt.common.channel:id/complete").click()
        driver.find_element_by_id("com.gt.common.channel:id/next_tv").click()
        time.sleep(2)
        driver.find_element_by_id("com.gt.common.channel:id/item_cl").click()
        time.sleep(1)
        # driver.find_element_by_id("com.gt.common.channel:id/image_iv").click()
        # driver.find_element_by_name(u"相册").click()
        # driver.find_element_by_id("com.gt.common.channel:id/image_view_album_image").click()
        # time.sleep(1)
        # driver.find_element_by_id("com.gt.common.channel:id/image_view_image_select").click()
        # driver.find_element_by_id("com.gt.common.channel:id/menu_item_add_image").click()
        # time.sleep(3)


        #上传贸易资料 订单1
        for element in driver.find_elements_by_id('com.gt.common.channel:id/image_iv'):
            element.click()
            driver.find_element_by_name(u"相册").click()
            driver.find_element_by_id("com.gt.common.channel:id/image_view_album_image").click()
            time.sleep(1)
            driver.find_element_by_id("com.gt.common.channel:id/image_view_image_select").click()
            driver.find_element_by_id("com.gt.common.channel:id/menu_item_add_image").click()
            time.sleep(3)

        driver.find_element_by_id("com.gt.common.channel:id/save").click()
        time.sleep(1)
        driver.find_element_by_id("com.gt.common.channel:id/add_order_tv").click()
        time.sleep(1)
        driver.find_element_by_name(u"订单 2").click()

        # 上传贸易资料 订单2
        for element in driver.find_elements_by_id('com.gt.common.channel:id/image_iv'):
            element.click()
            driver.find_element_by_name(u"相册").click()
            driver.find_element_by_id("com.gt.common.channel:id/image_view_album_image").click()
            time.sleep(1)
            driver.find_element_by_id("com.gt.common.channel:id/image_view_image_select").click()
            driver.find_element_by_id("com.gt.common.channel:id/menu_item_add_image").click()
            time.sleep(3)
        driver.find_element_by_id("com.gt.common.channel:id/save").click()
        driver.find_element_by_name(u"下一步").click()

        #填写采购计划1
        driver.find_element_by_id("com.gt.common.channel:id/item_cl").click()
        driver.find_element_by_id("com.gt.common.channel:id/editText2").send_keys('111111111')
        driver.find_element_by_id("com.gt.common.channel:id/editText").send_keys(u"这是一个非常流弊的产品哈哈哈哈11")
        driver.find_element_by_id("com.gt.common.channel:id/quantity_til").send_keys('111111111')
        driver.find_element_by_id("com.gt.common.channel:id/expected_price_til").send_keys('1111111111')
        driver.find_element_by_id("com.gt.common.channel:id/time_rl").click()
        time.sleep(1)
        driver.find_element_by_id("com.gt.common.channel:id/mdtp_ok").click()
        time1=driver.find_element_by_id("com.gt.common.channel:id/time_tv").text
        print time1
        driver.find_element_by_id("com.gt.common.channel:id/image_iv").click()
        driver.find_element_by_name(u"相册").click()
        driver.find_element_by_id("com.gt.common.channel:id/image_view_album_image").click()
        time.sleep(1)
        driver.find_element_by_id("com.gt.common.channel:id/image_view_image_select").click()
        driver.find_element_by_id("com.gt.common.channel:id/menu_item_add_image").click()
        time.sleep(3)

        driver.find_element_by_id("com.gt.common.channel:id/save").click()
        driver.find_element_by_name(u"下一步").click()

        #企业资料填写
        driver.find_element_by_name(u"企业形象照片").click()
        driver.find_element_by_name(u"相册").click()
        driver.find_element_by_id("com.gt.common.channel:id/image_view_album_image").click()
        time.sleep(1)
        driver.find_element_by_id("com.gt.common.channel:id/image_view_image_select").click()
        driver.find_element_by_id("com.gt.common.channel:id/menu_item_add_image").click()
        time.sleep(3)
        driver.find_element_by_name(u"样品间或门店照片").click()
        driver.find_element_by_name(u"相册").click()
        driver.find_element_by_id("com.gt.common.channel:id/image_view_album_image").click()
        time.sleep(1)
        driver.find_element_by_id("com.gt.common.channel:id/image_view_image_select").click()
        driver.find_element_by_id("com.gt.common.channel:id/menu_item_add_image").click()
        time.sleep(3)
        driver.find_element_by_name(u"联系人照片").click()
        driver.find_element_by_name(u"相册").click()
        driver.find_element_by_id("com.gt.common.channel:id/image_view_album_image").click()
        time.sleep(1)
        driver.find_element_by_id("com.gt.common.channel:id/image_view_image_select").click()
        driver.find_element_by_id("com.gt.common.channel:id/menu_item_add_image").click()
        time.sleep(3)
        driver.find_element_by_id("com.gt.common.channel:id/next_tv").click()




















if __name__ == '__main__':
    unittest.main()


