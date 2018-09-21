#coding=utf-8
from selenium import webdriver
import unittest,HTMLTestRunner,time,testDemo
testunit=unittest.TestSuite()
testunit.addTest(unittest.makeSuite(testDemo.DpAppTests))
#执行测试套件
now = time.strftime("%Y-%m-%M-%H_%M_%S",time.localtime(time.time()))
filename="C:\\Python27\\Yuanjunling\\YUAN\\"+now+'baogao.html'
fp = file(filename,'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u"渠道助手测试报告",
    description=u"用例执行情况"
)
runner.run(testunit)

