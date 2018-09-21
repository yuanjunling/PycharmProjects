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

browser=webdriver.Chrome()
browser.maximize_window()
browser.get("https://cas.qa.great-tao.com:8443/cas-server/login?service=http://boss.qa.great-tao.com/cas")
browser.implicitly_wait(30)
browser.find_element_by_id("username").send_keys("yuan")
browser.find_element_by_id("password").send_keys("1234")
browser.find_element_by_id("captcha").send_keys("greattao0818")
browser.find_element_by_id("captcha").send_keys(Keys.ENTER)
time.sleep(2)
browser.find_element_by_xpath(".//*[@id='Hui-nav']/ul/li[2]/a").click()
time.sleep(2)
browser.find_element_by_xpath(".//*[@id='menu2']/li/a").click()
time.sleep(2)
browser.find_element_by_xpath(".//*[@id='menu2']/li/ul/li[6]/a").click()
time.sleep(2)
#从frame中切回主文档
browser.switch_to.default_content()
browser.switch_to.frame(1)
ttt="融资线索"
Select(browser.find_element_by_id("type")).select_by_visible_text(ttt)
Select(browser.find_element_by_id("source")).select_by_visible_text("互联网（线上运营）")
browser.find_element_by_id("sourceRemark").send_keys(u"的发生的发生地方")
browser.find_element_by_id("company").send_keys(u"z浙江融资公司")
browser.find_element_by_id("contact").send_keys(u"contact")
shuzi="180000000"
# browser.find_element_by_id("tel").send_keys(shuzi)
# browser.find_element_by_id("email").send_keys("261412489@qq.com")
browser.find_element_by_id("content").send_keys(u"测试.1111111..")
browser.find_element_by_id("btn-addAttach").click()
time.sleep(1)
browser.find_element_by_name("file").send_keys('E:/ipg/B`L~8YOF79OO%IHN~6JT@W0.png')
browser.find_element_by_id("submit").click()
#焦点集中到页面上的一个警告（提示）
browser.switch_to_alert()
browser.switch_to_alert().dismiss()
# browser.accept()
time.sleep(2)

#找到该选择项元素
status=browser.find_element_by_xpath(".//*[@id='type']")
# 点击元素
status.click()
# .options方法获得所有可选项,是一个元素对象列表
ret=Select(status).options
# ret[1:]表示从列表中剔除第一个选项，因为第一个一般为请选择，不是实际的选项;random.Random().choice方法是python自带的，可以从一个序列中随机选择一个值
# srand = random.Random().choice(ret[1:])
srand =random.Random().choice(ret[1:])
#srand.get_attribute("value")得到选项的value，用Select.select_by_value方法选择该等于该值的选项
Select(status).select_by_value(srand.get_attribute("value"))
browser.find_element_by_id("btn_query").click()
time.sleep(2)
#相当于后退的方法，我们可以随意切换不同的frame
browser.switch_to.parent_frame()

browser.find_element_by_xpath(".//*[@id='menu2']/li/ul/li[1]/a").click()
time.sleep(2)
browser.switch_to.default_content()
browser.switch_to.frame(2)
browser.find_element_by_xpath(".//*[@id='table']/tbody/tr/td[7]/a").click()
now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
wwwa ='C:\\Python27\\Yuanjunling\\YUAN\\'+now+'result.html'
fp = file(wwwa,'wb')
# 定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(

    stream=fp,
    title=u"渠道助手测试报告",
    description=u"用例执行情况："
    )

