#coding=utf-8
import requests
import re
import unittest
import pymysql
import json
import HTMLTestRunner
import random,time,sys

class ApiQudzs(unittest.TestCase):
    global s
    s = requests.Session()  # 保持Cookie
    def setUp(self):
        self.log = 'https://login.dev.egtcp.com/cas-server/login?service=https://channel.dev.egtcp.com/cas'#渠道助手端登录网址

    def test_log(self):
        log_url = self.log



