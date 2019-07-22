#coding=utf-8
import requests
import re
import unittest
import pymysql
import json
import random,time,sys,string

class Apiyy(unittest.TestCase):
    def setUp(self):
        self.GetInspectionList = "http://ptest.tsescloud.com:31008/Patrol/PatrolInspection/GetInspectionList"
        self.log = "http://ptest.tsescloud.com:31001/api/User/Login"
        self.GetMyInspectionList = "http://ptest.tsescloud.com:31008/Patrol/PatrolInspection/GetMyInspectionList"
        self.AddInspection = "http://192.168.200.7:31008/Patrol/PatrolInspection/AddInspection"
    def test_a_log(self):
        '''api自动化登录'''
        logurl = self.log
        json_test = {
            "UserName": "13613613602",
            "PassWord": "111111",
            "Endpoint": "1"
        }
        headers = {"Content-Type": "application/json; charset=utf-8"}
        global Data
        Data = requests.post(logurl, json=json_test, headers=headers).json()
        Data["Data"]

    def test_b_GetInspectionList(self):
        url = self.GetInspectionList
        json_test={"Page": "1","Num": "10" }
        headers = {"Content-Type":"application/json; charset=utf-8","Authorization":Data["Data"]}
        r1 = requests.post(url,json=json_test,headers=headers).json()
        json.dumps(r1,ensure_ascii=False)
        self.assertEqual(r1["Msg"],u"获取成功")

    def test_c_GetMyInspectionList(self):
        url = self.GetMyInspectionList
        headers = { "Authorization": Data["Data"]}
        payload = {"Page":"1","Num":"10","Key":"清洁","Type":"1"}
        r1 = requests.get(url,headers=headers,params=payload).json()
        json.dumps(r1,ensure_ascii=False)
        self.assertEqual(r1["Msg"], u"获取成功")
    def test_d_AddInspection(self):#添加扣分项
        url = self.AddInspection
        headers = {"Content-Type": "application/json","Authorization": Data["Data"],"accept":"*/*"}
        global random1
        random1 = ''.join(random.sample(string.ascii_letters + string.digits, 50))  # 随机生成字符串
        json_test = {"DMBGuid":"3fjEAi4SLuM","ISSGuid":"3ejiuxPPjwm","ISContent":random1}
        r1 = requests.post(url,json=json_test,headers=headers).json()
        json.dumps(r1, ensure_ascii=False)
        self.assertEqual(r1["Msg"], u"操作成功")

if __name__ == '__main__':
    unittest.main()

