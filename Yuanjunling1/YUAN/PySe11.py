#coding=utf-8
from pyse import Pyse
from time import sleep
driver = Pyse("chrome")
driver.open("https://www.baidu.com")
driver.clear("id=>kw")
#id定位
#driver.type("id=>kw", "pyse")
#name定位
#driver.type("name=>wd","pyse")
#link text定位：点击百度首页上面的“新闻”链接（有问题）
driver.click_text(u"link_text=>新闻")
#class定位
#driver.type("xpath=>//*[class='s_ipt']","pyse")
#xpath定位
#driver.type("xpath=>//*[@id='kw']","pyse")
#driver.click("xpath=>//*[@id='su']")
#css定位
#driver.type("css=>.s_ipt","pyse")
#driver.type("css=>#su","pyse")
#driver.click("css=>#su")
sleep(20)
#self.assertTrue("pyse",driver.get_title())
driver.quit()