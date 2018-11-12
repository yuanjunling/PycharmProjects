#coding=utf-8
import requests
import re
import unittest
import pymysql
import json
import random,time,sys

class ApiQudzs(unittest.TestCase):



    def setUp(self):
        self.log = 'https://login.dev.egtcp.com/cas-server/login?service=https://channel.dev.egtcp.com/cas'#渠道助手端登录网址
        self.url = 'https://channel.dev.egtcp.com/channel/index?messageCount=31&qrcodeUrl=http%3A%2F%2Ft.cn%2FRr6wq9Y&locale=zh_CN'
        self.apilog = 'https://account.dev.egtcp.com/api/user/login'



    def testAddSupplier(self):

        url = self.url
        log_test()#登录函数
        a1 = s.get(url)


        #断言验证的账号密码验证码
        self.assertEqual(test_json['username'],'yuanjlll')
        self.assertEqual(test_json['password'],'111111')
        self.assertEqual(test_json['captcha'],'greattao0818')
        self.assertIn(b"https://channel.dev.egtcp.com",a1.content)
        self.assertEqual(a1.status_code,200)


    def testAddBuyer(self):
        log_test()
        r = s.get("https://channel.dev.egtcp.com/channel/customer/new")





def log_test():
    global s
    s = requests.Session()  # 保持Cookie
    global test_json
    global a

    apilog = 'https://account.dev.egtcp.com/api/user/login'
    test_json = {'username': 'yuanjlll',
                 'password': '111111',
                 'captcha': 'greattao0818',
                 }
    s.post(apilog, json=test_json,
           )  # POST帐号和密码，

    return





if __name__ == '__main__':
    unittest.main()









