#coding=utf-8
import requests
import re
import unittest
import pymysql
import json
import random,time,sys

class ApiQudzs(unittest.TestCase):
    global s
    s = requests.Session()  # 保持Cookie
    def setUp(self):
        self.log = 'https://login.dev.egtcp.com/cas-server/login?service=https://channel.dev.egtcp.com/cas'#渠道助手端登录网址
        self.url = 'https://channel.dev.egtcp.com/channel/index?messageCount=31&qrcodeUrl=http%3A%2F%2Ft.cn%2FRr6wq9Y&locale=zh_CN'
        self.apilog = 'https://account.dev.egtcp.com/api/user/login'

    def test_log(self):
        apilog = self.apilog
        log_url = self.log
        url = self.url
        # a1 = s.get(log_url).content  # 获取页面源码
        # lt1 = re.search('name="lt" value="(.*)"', a1).group(1)  # 查找源码中的lt
        # execution1 = re.search('name="execution" value="(.*)"', a1).group(1)
        # 登录渠道助手系统
        test_json={'username': 'yuanjlll',
                  'password': '111111',
                  'captcha': 'greattao0818',
                            }
        s.post(apilog, json=test_json,
               )  # POST帐号和密码，
        r = s.get(url)
        #断言验证的账号密码验证码
        self.assertEqual(test_json['username'],'yuanjlll')
        self.assertEqual(test_json['password'],'111111')
        self.assertEqual(test_json['captcha'],'greattao0818')
        self.assertIn(b"https://channel.dev.egtcp.com",r.content)
        self.assertEqual(r.status_code,200)






