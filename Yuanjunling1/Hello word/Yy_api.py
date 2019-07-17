#coding=utf-8
import requests
import re
import unittest
import pymysql
import json
import random,time,sys,string

logurl = "http://ptest.tsescloud.com:31001/api/User/Login"
json_test = {
    "UserName": "13613613602",
    "PassWord": "111111",
    "Endpoint": "1"
}
headers = {"Content-Type": "application/json; charset=utf-8"}
global Data
Data = requests.post(logurl, json=json_test, headers=headers).json()
print Data["Data"]

class Apiyy(unittest.TestCase):
    def setUp(self):
        self.GetInspectionList = "http://ptest.tsescloud.com:31008/Patrol/PatrolInspection/GetInspectionList"

    def test_GetInspectionList(self):

        url = self.GetInspectionList

        json_test={
            "Page": "1",
            "Num": "10",
        }
        headers = {
            "Content-Type":"application/json; charset=utf-8",
            "Authorization":Data["Data"]
        }
        r1 = requests.post(url,json=json_test,headers=headers).json()
        print json.dumps(r1,ensure_ascii=False)
        self.assertEqual(r1["Msg"],u"获取成功")




