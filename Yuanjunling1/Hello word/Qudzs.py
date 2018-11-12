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
        #验证供应商名称是否重复
        r = s.get("https://channel.dev.egtcp.com/channel/customer/new")
        self.assertIn(b"Hamilton Watkins",r.content)
        Suppliername1 = u'供应商测试数据%d'%random.randrange(1, 9999,)
        Suppliername = {'customerName':Suppliername1,'role':'2'}
        add = s.post("https://channel.dev.egtcp.com/channel/customer/checkname",data=Suppliername)
        #供应商数据
        Supplier = {
            'address':u'地址',
            'company':Suppliername1,
            'contactEmail':'261412489@qq.com',
            'contactMobileNumber':random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8)),
            'contactName':random.choice( [u"奥特曼", u"舞法美少女", u"关公",u"张飞", u"奥黛丽赫本",u"朱茵"]),
            'customerName':Suppliername1,
            'customerRequirements':'1',
            'customerRequirements':'2',
            'customerRequirements':'8',
            'district':'330523',
            'industry':'20',
            'province':'330000',
            'role':'2',
            'shi':'330500',
            'status':'3',
            'test':'20',
            'status':'4',
        }
        #添加供应商
        s.post("https://channel.dev.egtcp.com/channel/customer",data=Supplier)
        self.assertEqual(Supplier['customerName'],Suppliername1)




    def testAddBuyer(self):
        log_test()






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









