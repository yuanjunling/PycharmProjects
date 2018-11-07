#coding=utf-8
import requests
import unittest
from HTMLTestRunner import HTMLTestRunner
import APIBOSS,time



testunit = unittest.TestSuite()
#将测试用例加入到测试套件中
testunit.addTest(unittest.makeSuite(APIBOSS.ApiBossTest))
# #定义个报告存放路径，支持相对路径。
now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
wwwa ='D:\\apitest'+now+'result.html'

fp = file(wwwa,'wb')
runner = HTMLTestRunner(

    stream=fp,
    title=u"渠道助手测试报告",
    description=u"用例执行情况：",
    verbosity=2
)
#执行测试用例
# runner = unittest.TextTestRunner()
runner.run(testunit)
fp.close()