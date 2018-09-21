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
import unittest, time, re ,random,os,sys,xlrd, HTMLTestRunner,login


def Drop_box(driver):
    status = driver.find_element_by_id("province")
    status.click()
    ret = Select(status).options
    srand = random.Random().choice(ret[1:])
    Select(status).select_by_value(srand.get_attribute("value"))

    status = driver.find_element_by_id("city")
    status.click()
    ret = Select(status).options
    srand = random.Random().choice(ret[1:])
    Select(status).select_by_value(srand.get_attribute("value"))

    status = driver.find_element_by_id("district")
    status.click()
    ret = Select(status).options
    srand = random.Random().choice(ret[1:])
    Select(status).select_by_value(srand.get_attribute("value"))
    return

class Boss(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.Boss_url = "http://boss.dev.great-tao.com/"
        self.verificationErrors=[]
        self.accept_next_alet=True


    def test_Guonei(self):
        u"""创建国内渠道"""
        driver = self.driver
        driver.get(self.Boss_url)
        driver.maximize_window()
        driver.implicitly_wait(30)
        #登录BOSS系统
        login.login(driver)
        nowhandle = driver.current_window_handle
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='Hui-nav']/ul/li[1]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='menu2']/li[11]/a").click()
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='menu2']/li[11]/ul/li[1]/a").click()
        # 从frame中切回主文档
        driver.switch_to.default_content()
        driver.switch_to_frame(1)
        #创建国内渠道
        try:
            driver.find_element_by_xpath("html/body/div[1]/div[1]/div/div[1]/div/a").click()
            driver.find_element_by_id("agent").send_keys(random.choice( ['apple', 'pear', 'peach', 'orange', 'lemon']))
            driver.find_element_by_id("legalPerson").send_keys(random.choice( [u"奥特曼", u"舞法美少女", u"关公",u"张飞", u"奥黛丽赫本",u"朱茵"]))
            driver.find_element_by_id("tel").send_keys(random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8)))
            driver.find_element_by_id("email").send_keys("261412489@qq.com")

            driver.find_element_by_id("margin").send_keys("5000")
            driver.find_element_by_id("initialFee").send_keys("5000")
            # driver.find_element_by_id("beginTime").send_keys("2017-04-01")
            driver.find_element_by_id("beginTime").click()
            driver.find_element_by_xpath("html/body/div[2]/div[3]/table/tfoot/tr/th").click()
            driver.find_element_by_id("timeLimit").send_keys(random.randrange(1, 99, ))
            time.sleep(2)
            driver.find_element_by_class_name("webuploader-element-invisible").send_keys("E:\ipg\popoo.jpeg")
            time.sleep(3)
            qudao=u"渠道名称%d"%random.randrange(1, 9999, )
            driver.find_element_by_id("name").send_keys(qudao)
            Select(driver.find_element_by_id("managerId")).select_by_index(5)
            random1=random.choice(['adv','mid','pri'])
            driver.find_element_by_id(random1).click()
            # driver.find_element_by_id("maxCustomer").clear()
            # driver.find_element_by_id("maxCustomer").send_keys("300")
            # driver.find_element_by_id("maxSubAccount").clear()
            # driver.find_element_by_id("maxSubAccount").send_keys("500")
            driver.find_element_by_id("password").clear()
            driver.find_element_by_id("password").send_keys("111111")
            if random1=='adv':
                advtest=u"adv%d"%random.randrange(1, 9999, )
                driver.find_element_by_id("username").send_keys(advtest)

                #选择省市区
                Drop_box(driver)
                time.sleep(1)




                driver.find_element_by_id("btn-add-area").click()
            elif random1=='mid':
                testmid=u"mid%d" % random.randrange(1, 9999, )
                driver.find_element_by_id("username").send_keys(testmid)


                #Select(driver.find_element_by_id("province")).select_by_value('330000')
                Drop_box(driver)


                driver.find_element_by_id("btn-add-area").click()
            else:
                testpri=u"pri%d" % random.randrange(1, 9999, )
                driver.find_element_by_id("username").send_keys(testpri)


            driver.find_element_by_id("btn-submit").click()
            time.sleep(2)
            driver.find_element_by_id("name").send_keys(qudao)
            driver.find_element_by_id("btn_query").click()
            time.sleep(1)
            driver.find_element_by_xpath(".//*[@id='tab1']/div/div[1]/div[2]/div[2]/table/tbody/tr/td[14]/a[1]").click()
            driver.switch_to.default_content()
            driver.switch_to_frame(2)
            # qdzh= driver.find_element_by_xpath("html/body/div[1]/div/div/div/div[4]/label").text
            # print qdzh
            qdzh = driver.find_element_by_xpath("html/body/div[1]/div/div/div/div[4]/label").text
            print qdzh





            js='window.open("http://channel.qa.egtcp.com/")'
            driver.execute_script(js)
            allhandles = driver.window_handles
            allhandle = driver.window_handles
            for handle in allhandle:
                if handle != nowhandle:
                    driver.switch_to_window(handle)

                print handle
                time.sleep(1)

            driver.find_element_by_id("username").send_keys(qdzh)
            driver.find_element_by_id("password").send_keys("111111")
            driver.find_element_by_id("captcha").send_keys("greattao0818")
            driver.find_element_by_id("captcha").send_keys(Keys.ENTER)
            time.sleep(1)
            # driver.find_element_by_name(u"客户管理 									").click()
            # time.sleep(1)
            driver.find_element_by_xpath(".//*[@id='sidebar-menu']/div/ul/li[1]/ul/li[4]/a").click()
            time.sleep(1)
            driver.find_element_by_name("company").send_keys(u"浙江舟山外贸集团%d"%random.randrange(1, 9999,))
            Drop_box.Drop_box(driver)
            driver.find_element_by_name("address").send_keys(u"浙江宁波鄞州区")
            #选择客户需求
            status1 = driver.find_element_by_id("requirement")
            status1.click()
            ret = Select(status1).options
            srand = random.Random().choice(ret[1:])
            Select(status1).select_by_value(srand.get_attribute("value"))
            time.sleep(1)
            #选择客户类型
            status2 = driver.find_element_by_name("type")

            status2.click()
            ret = Select(status2).options
            srand = random.Random().choice(ret[1:])
            Select(status2).select_by_value(srand.get_attribute("value"))
            #选择行业name=industry
            status3 = driver.find_element_by_name("industry")
            status3.click()
            ret = Select(status3).options
            srand = random.Random().choice(ret[1:])
            Select(status3).select_by_value(srand.get_attribute("value"))
            driver.find_element_by_name("contactName").send_keys(u"老六")
            driver.find_element_by_name("contactEmail").send_keys(random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))+"@qq.com")
            driver.find_element_by_name("contactMobileNumber").send_keys(random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8)))
            











        except:
            now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
            driver.get_screenshot_as_file(u"E:\\工作任务\异常截图\\"+now+"error_png.png")






    # def test_Guowai(self):
    #     driver = self.driver
    #     driver.get(self.Boss_url)
    #     driver.maximize_window()
    #     driver.implicitly_wait(30)




    def is_element_present(self,how,what):
         try:
             self.driver.find_element(by=how,value=what)
         except NoSuchElementException,e :return  False
         return True



    # def tearDown(self):
    #     self.driver.quit()
    #     self.assertEqual([], self.verificationErrors)
if __name__=="__main__":
    unittest.main()
    # 定义一个单元测试容器
    # testunit = unittest.TestSuite()
    # 将测试用例加入到测试容器中
    # testunit.addTest(Boss("test_Guonei"))
    # 定义个报告存放路径，支持相对路
    # now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    # wwwa ='C:\\Python27\\Yuanjunling\\YUAN\\'+now+'result.html'
    # fp = file(wwwa,'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(

        stream=fp,
        title=u"渠道助手测试报告",
        description=u"用例执行情况："
    )
    # runner.run(testunit)





