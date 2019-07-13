#coding=utf-8
import requests
import re
import unittest
import pymysql
import json
import random,time,sys
reload(sys)
sys.setdefaultencoding('utf8')
s = requests.Session()#保持Cookie
url = 'http://192.168.200.7:30501/api/User/Login'
headers = {
    "Content-Type":"application/json; charset=utf-8"
}
test_json={"UserName": "13613613602","PassWord": "111111","Endpoint": "1"}
json_Deom=s.post('http://192.168.200.7:30501/api/User/Login',headers=headers,json=test_json)
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
url1="http://192.168.200.7:30508/patrol/PatrolInspection/GetInspectionList"
# print s.post(url1,headers=headers1,json=test_json1).json()
jj= requests.post(url1,headers=headers1,json=test_json1).json()
# jjj = json.dumps(jj,ensure_ascii=False)
# print jj["Msg"]
#接口返回值断言

if jj["Msg"] == u"获取成功":
    print u"断言成功"
else:
    print u"断言失败"
assert jj["Msg"] == "获取成功"