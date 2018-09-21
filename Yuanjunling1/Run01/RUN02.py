#coding:utf-8

from lib import HTMLTestRunner
import unittest
from canshuhua import WidgetTestCase

if __name__ == "__main__":
    suite = unittest.makeSuite(WidgetTestCase)
    testunit = unittest.TestSuite()
    testunit.addTest(BaiduTest('test_baidu_search'))
    # 定义报告输出路径
    filename = 'testReport.html'
    fp = file(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u"百度测试",
        description=u"测试用例结果")
    runner.run(testunit)
    fp.close()