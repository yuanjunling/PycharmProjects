#coding=utf-8
import requests
import re
import unittest
import pymysql
import json
import random,time,sys

class Api_Xs(unittest.TestCase):

    reload(sys)
    sys.setdefaultencoding('utf8')
    global s
    s = requests.Session()#保持Cookie

    def setUp(self):
        self.url = 'http://ptest.tsescloud.com:31001/api/User/Login'
        self.url1 = "http://ptest.tsescloud.com:31008/Patrol/PatrolInspection/GetInspectionList"

    def Test_Xs(self):
        url = self.url
        url1=self.url1

        headers = {
        "Content-Type":"application/json; charset=utf-8"
        }
        test_json={"UserName": "13513513501","PassWord": "111111","Endpoint": "1"}
        json_Deom=s.post(url,headers=headers,json=test_json)
        key=json_Deom.json()
        print key["Data"]
        headers1 = {
            "Content-Type":"application/json; charset=utf-8",
            "Authorization":key["Data"]
        }
        test_json1={
            "Page":1,
            "Num":1
        }

        # print s.post(url1,headers=headers1,json=test_json1).json()
        jj= requests.post(url1,headers=headers1,json=test_json1).json()
        # jjj = json.dumps(jj,ensure_ascii=False)
        # print jj["Msg"]
        #接口返回值断言

        # if jj["Msg"] == u"获取成功":
        #     print u"断言成功"
        # else:
        #     print u"断言失败"
        self.assertAlmostEqual(jj["Msg"],'获取成功')