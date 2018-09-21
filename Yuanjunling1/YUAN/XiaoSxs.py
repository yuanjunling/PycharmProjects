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
import unittest, time, re ,random,os,sys,xlrd, HTMLParser,login
now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
class xiaosxx(unittest.TestCase):

    def setUp(self):

        self.driver=webdriver.Chrome()
        self.xiaosxx_url='http://boss.qa.great-tao.com'
        self.email_url='http://qiye.163.com/login/'
        self.verificationErrors = []
        self.accept_next_alet = True
    def test_xiaosxx(self):
        u"""创建采购线索"""
        driver=self.driver
        driver.get(self.xiaosxx_url)
        driver.maximize_window()
        driver.implicitly_wait(30)
        # 登录BOSS系统
        login.login(driver)
        nowhandle = driver.current_window_handle
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='Hui-nav']/ul/li[1]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='menu2']/li[10]/a").click()
        time.sleep(1)
        driver.find_element_by_xpath(".//*[@id='menu2']/li[10]/ul/li[6]/a").click()
        driver.refresh()  # 刷新方法 refresh
        # 从frame中切回主文档
        driver.switch_to.default_content()
        driver.switch_to_frame(1)

        time.sleep(2)

        try:

            #添加线索
            Select(driver.find_element_by_id("type")).select_by_index(1)
            Select(driver.find_element_by_id("source")).select_by_index(1)
            driver.find_element_by_id("sourceRemark").send_keys(random.choice([u'展销会',u'网络',u'QQ',]))
            Select(driver.find_element_by_id("roleBack")).select_by_index(1)
            driver.find_element_by_id("company").send_keys(u"老六麻辣烫%d"%random.randrange(1, 9999, ))
            driver.find_element_by_id("contact").send_keys(random.choice([u"奥特曼", u"舞法美少女", u"关公",u"张飞", u"奥黛丽赫本"]))
            driver.find_element_by_id("position").send_keys(u"销售")
            driver.find_element_by_id("tel").send_keys(random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8)))
            driver.find_element_by_id("email").send_keys("261412489@qq.com")
            driver.find_element_by_id("other").send_keys(u"手机")
            driver.find_element_by_id("content").send_keys("============================================================================================================")
            driver.find_element_by_id("btn-addAttach").click()
            driver.find_element_by_class_name("webuploader-element-invisible").send_keys("E:\ipg\popoo.jpeg")
            time.sleep(2)
            driver.find_element_by_id("submit").click()
            driver.find_element_by_xpath(".//*[@id='form']/div[3]/div[1]/button").click()

            driver.switch_to.frame(0)
            driver.find_element_by_id("name").send_keys(random.randrange(1,99999))
            driver.find_element_by_id("discription").send_keys(random.randrange(1,999999))
            driver.find_element_by_id("specification").send_keys(random.randrange(1,999999))
            driver.find_element_by_id("purNumber").send_keys(random.randrange(1,999999))
            driver.find_element_by_id("argument").send_keys(random.randrange(1,999999))
            driver.find_element_by_id("purpose").send_keys(random.randrange(1,999999))
            driver.find_element_by_id("targetPrice").send_keys("555555")
            driver.find_element_by_id("orderTime").click()
            driver.find_element_by_xpath("html/body/div[1]/div[3]/table/tfoot/tr/th").click()
            driver.find_element_by_xpath(".//*[@id='form']/div[3]/div[3]/div/div/div/p[3]/button").click()
            driver.find_element_by_class_name("webuploader-element-invisible").send_keys("E:\ipg\popoo.jpeg")
            time.sleep(2)
            driver.find_element_by_id("submit").click()
            time.sleep(2)
            driver.switch_to.frame(1)
            driver.find_element_by_xpath(".//*[@id='submit']").click()


        except:

            driver.get_screenshot_as_file(u"E:\\工作任务\异常截图\\" + now + "error_png.png")

        try:
            #采购线索分配
            a=driver.find_element_by_xpath(".//*[@id='table']/tbody/tr[1]/td[2]").text
            print a
            driver.switch_to.default_content()
            time.sleep(1)
            #11111111
            driver.find_element_by_xpath(".//*[@id='Hui-nav']/ul/li[2]/a").click()
            time.sleep(1)
            driver.find_element_by_xpath(".//*[@id='menu2']/li[11]/a").click()
            time.sleep(1)
            #1111111
            driver.find_element_by_xpath(".//*[@id='menu2']/li[11]/ul/li[4]/a").click()
            driver.switch_to_frame(2)
            driver.find_element_by_id("leadsNo").send_keys(a)
            driver.find_element_by_id("btn_query").click()
            driver.find_element_by_xpath(".//*[@id='table']/tbody/tr/td[11]/a[2]").click()
            driver.switch_to_frame(0)
            Select(driver.find_element_by_id("receiver")).select_by_value('61')
            Select(driver.find_element_by_id("domesticBuyerId")).select_by_value('61')
            driver.find_element_by_id("confirm").click()
        except:
            driver.get_screenshot_as_file(u"E:\\工作任务\异常截图\\" + now + "error_png.png")
        try:
            #采购对接线索
            driver.switch_to.default_content()
            driver.find_element_by_xpath(".//*[@id='menu2']/li[11]/ul/li[1]/a").click()
            driver.switch_to_frame(3)
            time.sleep(2)
            driver.find_element_by_xpath(".//*[@id='table']/tbody/tr[1]/td[8]/a").click()
            time.sleep(2)
            driver.switch_to.default_content()
            driver.switch_to_frame(4)
            time.sleep(2)
            Bianhao=driver.find_element_by_xpath("html/body/div[1]/div/div/div[2]/dt[2]").text

            if a==Bianhao:
                print "线索编号正确"
            else:
                print "线索编号错误"
                # 待关联
            driver.find_element_by_id("edit1").click()
            driver.switch_to_frame(0)
            driver.find_element_by_xpath(".//*[@id='table']/tbody/tr[4]/td[1]/input").click()
            driver.find_element_by_id("confirm").click()
            driver.switch_to_frame(4)
            driver.find_element_by_id("edit2").click()
            driver.switch_to_frame(0)
            #待跟进
            ccc=random.choice([u"一般客户",u"潜在客户",u"优质客户",u"待签客户"])
            Select(driver.find_element_by_id("customerType")).select_by_value(ccc)
            driver.find_element_by_id("followupRemark").send_keys("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
            driver.find_element_by_id("followupDate").click()
            driver.find_element_by_xpath("html/body/div[2]/div[3]/table/tfoot/tr/th").click()
            driver.find_element_by_id("confirm").click()
            driver.switch_to_frame(4)
            #确认线索
            driver.find_element_by_id("edit6").click()
            time.sleep(1)
            driver.find_element_by_xpath(".//*[@id='layui-layer1']/div[3]/a[1]").click()
           #进入报价池
            driver.switch_to.default_content()
            time.sleep(1)
            driver.find_element_by_xpath(".//*[@id='menu2']/li[11]/ul/li[7]/a").click()
            driver.switch_to_frame(5)
            driver.find_element_by_id("leadsNo").send_keys(a)
            driver.find_element_by_id("btn_query").click()
            time.sleep(1)
            driver.find_element_by_xpath(".//*[@id='table']/tbody/tr/td[10]/a").click()
            driver.switch_to.default_content()
            driver.switch_to_frame(6)
            driver.find_element_by_xpath(".//*[@id='productlist']/tr/td[1]/input").click()
            time.sleep(1)
            driver.find_element_by_id("selectbtn").click()
            driver.find_element_by_id("params").send_keys(u"供应商测试啊")
            time.sleep(1)
            driver.find_element_by_id("btn_query1").click()
            time.sleep(1)
            driver.find_element_by_name("btSelectItem").click()
            time.sleep(1)
            driver.find_element_by_class_name("layui-layer-btn0").click()
            time.sleep(1)
            driver.find_element_by_name("btSelectItem").click()
            time.sleep(1)
            driver.find_element_by_id("btnSend").click()
            time.sleep(1)
            baojia_id=driver.find_element_by_xpath("html/body/div[1]/div/div[4]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr/td[13]").text
            print baojia_id

            #供应商填写报价单
            js = 'window.open("http://boss.qa.great-tao.com/boss-leads-web/offer/out/%s")'%baojia_id

            driver.execute_script(js)
            allhandles = driver.window_handles
            allhandle=driver.window_handles
            for handle in allhandle:
                if handle != nowhandle:
                    driver.switch_to_window(handle)

                print handle

            Gsmc = driver.find_element_by_xpath("html/body/div[1]/div[1]/div/div[2]/h2").text
            print Gsmc
            if Gsmc == u"浙江大道众包电商股份有限公司报价单":
                print "公司名称正确"
            else:
                print "公司名称错误"
            driver.find_element_by_id("companyName").send_keys(u"超级大大供应商%s"%random.randrange(1,99999))
            driver.find_element_by_id("companyAddress").send_keys(u"浙江宁波鄞州区")
            Select(driver.find_element_by_id("paymentWay")).select_by_index(1)
            Select(driver.find_element_by_id("tradeWay")).select_by_index(0)
            driver.find_element_by_id("place0").send_keys(u"宁波")
            driver.find_element_by_id("moq0").send_keys(random.randrange(1,9999999))
            driver.find_element_by_id("ltpes[0].productionCycle").send_keys("20170903")
            packing0=random.choice([u"集装箱",u"散装",u"陆运",u"空运"])
            driver.find_element_by_id("packing0").send_keys(packing0)
            driver.find_element_by_id("price0").send_keys(random.randrange(1,999999))
            driver.find_element_by_id("weight0").send_keys("232323")
            driver.find_element_by_id("remark0").send_keys("======================+++++")
            driver.find_element_by_id("submitForm").click()

            time.sleep(2)
            driver.close()
            driver.switch_to_window(nowhandle)
            driver.switch_to_frame(6)
            time.sleep(1)
            driver.find_element_by_name("refresh").click()

            driver.find_element_by_link_text(u"查看报价").click()
            time.sleep(1)
            driver.switch_to.default_content()
            driver.switch_to_frame(7)
            time.sleep(1)
            driver.find_element_by_id("confirmByBuyer").click()
            driver.switch_to.default_content()
            driver.find_element_by_xpath(".//*[@id='min_title_list']/li[4]/span").click()
            driver.switch_to_frame(3)
            driver.find_element_by_id("leadsNo").send_keys(a)
            driver.find_element_by_id("btn_query").click()


        except:
            driver.get_screenshot_as_file(u"E:\\工作任务\异常截图\\" + now + "error_png.png")




            # def test_email(self):
    #  driver = self.driverx`
    #  driver.get(self.email_url)
    #  driver.maximize_window()
    #  driver.implicitly_wait(30)
         #登录企业邮箱


            #获得所有窗口
            # allhandle=driver.window_handles
            # for handle in allhandle:
            #     if handle != nowhandle:
            #         driver.switch_to_window(handle)
            #
            #     print handle










