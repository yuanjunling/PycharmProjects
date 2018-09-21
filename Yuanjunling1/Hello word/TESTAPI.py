#coding=utf-8
import requests
import re
import unittest
#import MySQLdb
import logging




login_url = 'https://cas.dev.great-tao.com/cas-server/login?service=http://boss.dev.great-tao.com/cas'
url1 = 'http://boss.dev.great-tao.com/'


headers={'Content-Encoding': 'gzip', 'Transfer-Encoding': 'chunked',  'Expires': 'Thu, 01 Jan 1970 00:00:00 GMT', 'Vary': 'Accept-Encoding', 'Server': 'nginx', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Cache-Control': 'no-cache, no-store', 'Content-Type': 'text/html;charset=UTF-8'}

a1 = requests.get(login_url).content  # 获取页面源码
lt1 = re.search('name="lt" value="(.*)"', a1).group(1)  # 查找源码中的lt
execution1 = re.search('name="execution" value="(.*)"', a1).group(1)

s = requests.Session()  # 保持Cookie
response = s.post(login_url, {'username': 'yuanjunling', 'password': '1234', 'captcha': 'greattao0818', 'submit': 'LOGIN','_eventId': 'submit', 'lt':lt1, 'execution': execution1,},headers=headers)  # POST帐号和密码，设置headers
#result = s.get(url1,cookies = response.cookies)
print response.text
# print response.cookies
# print lt1
# print execution1
# r = s.get(url1)  # 已经是登录状态了
# print r.text



