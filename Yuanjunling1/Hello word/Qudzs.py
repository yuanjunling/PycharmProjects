#coding=utf-8
import requests
import re
import unittest
import pymysql
import json
import random,time,sys,string,ddt
s = requests.Session()#保持Cookie
#测试数据
random1 =''.join(random.sample(string.ascii_letters + string.digits, 50))#随机生成字符串
Suppliername1 = u'供应商测试数据%d'%random.randrange(1, 9999,)
Supplier = [
{
            'address':random1,
            'company':Suppliername1,
            'contactEmail':' @qq.com',
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
        },
{
            'address':random1,
            'company':u'供应商测试数据%d'%random.randrange(1, 99999,),
            'contactEmail':' @qq.com',
            'contactMobileNumber':random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8)),
            'contactName':random.choice( [u"奥特曼", u"舞法美少女", u"关公",u"张飞", u"奥黛丽赫本",u"朱茵"]),
            'customerName':u'供应商测试数据%d'%random.randrange(1, 99999,),
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
        },
{
            'address':random1,
            'company':u'供应商测试数据%d'%random.randrange(1, 99999,),
            'contactEmail':' @qq.com',
            'contactMobileNumber':random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8)),
            'contactName':random.choice( [u"奥特曼", u"舞法美少女", u"关公",u"张飞", u"奥黛丽赫本",u"朱茵"]),
            'customerName':u'供应商测试数据%d'%random.randrange(1, 99999,),
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


]
@ddt.ddt
class ApiQudzs(unittest.TestCase):
    def setUp(self):
        self.log = 'https://login.dev.egtcp.com/cas-server/login?service=https://channel.dev.egtcp.com/cas'#渠道助手端登录网址
        self.url = 'https://channel.dev.egtcp.com/channel/index?messageCount=31&qrcodeUrl=http%3A%2F%2Ft.cn%2FRr6wq9Y&locale=zh_CN'
        self.apilog = 'https://account.dev.egtcp.com/api/user/login'

    @ddt.data(*Supplier)
    def testAddSupplier(self,Supplier):

        url = self.url
        log_test()#登录函数
        a1 = s.get(url)
        #断言验证的账号密码验证码
        self.assertEqual(test_json['username'],'yuanjlll')
        self.assertEqual(test_json['password'],'111111')
        self.assertEqual(test_json['captcha'],'greattao0818')
        self.assertIn(b"https://channel.dev.egtcp.com",a1.content)
        self.assertEqual(a1.status_code,200)

        r = s.get("https://channel.dev.egtcp.com/channel/customer/new")
        self.assertIn(b"Hamilton Watkins",r.content)
        # Suppliername1 = u'供应商测试数据%d'%random.randrange(1, 9999,)
        # 验证供应商名称是否重复
        Suppliername = {'customerName':Suppliername1,'role':'2'}
        add = s.post("https://channel.dev.egtcp.com/channel/customer/checkname",data=Suppliername)
        #添加供应商
        s.post("https://channel.dev.egtcp.com/channel/customer",data=Supplier)



    def testAddBuyer(self):
        log_test()
        print s.get("https://channel.dev.egtcp.com/channel/customer/new").text






def log_test():
    # global s
    # s = requests.Session()

    global test_json


    apilog = 'https://account.dev.egtcp.com/api/user/login'
    test_json = {'username': 'yuanjlll',
                 'password': '111111',
                 'captcha': 'greattao0818',
                 }
    s.post(apilog, json=test_json,
           )  # POST帐号和密码，

    return

def test_sql(sql, args=None):
    # 建立数据库连接

    conn = pymysql.connect(
        host='192.168.2.203',  # 远程主机的ip地址
        user='gt_user',  # 数据库用户名
        db='gttown_crm',  # 表名
        passwd='greatTao1314!@#$',  # 数据库密码
        port=3306,
        charset="utf8"
    )
    # 创建游标
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    # 执行sql
    cursor.execute(sql, [args])
    results = cursor.fetchall()
    # 提交，不然无法保存新建或者修改的数据
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return results




if __name__ == '__main__':
    unittest.main()









