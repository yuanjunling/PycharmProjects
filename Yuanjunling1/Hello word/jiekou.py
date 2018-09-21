#coding=utf-8
import requests
import re
import unittest
import pymysql
import json
import HTMLTestRunner
import random,time,sys
class ApiDemoTest(unittest.TestCase):
    '''登录BOSS系统'''
    def setUp(self):
        self.log = 'https://cas.dev.great-tao.com/cas-server/login?service=http://boss.dev.great-tao.com/cas'
        self.url = 'http://boss.dev.great-tao.com/index'
        self.urlgys = 'http://crm.dev.great-tao.com/channel/customer/save'



    def test_Boss(self):
        login_url = self.log
        url = self.url
        urlgys = self.urlgys
        s = requests.Session()  # 保持Cookie
        a1 = s.get(login_url).content#获取页面源码
        lt1=re.search('name="lt" value="(.*)" />',a1).group(1) #查找源码中的lt
        execution1=re.search('name="execution" value="(.*)" ',a1).group(1)
        #登录BOSS系统
        s.post(login_url, data={'username':'yuanjunling',
                                'password': '1234',
                                'captcha':'greattao0818',
                                'submit':'LOGIN',
                                 '_eventId':'submit',
                                'lt':lt1,
                                'execution':execution1},
               )  # POST帐号和密码，设置headers
        print 'lt= '+lt1
        print 'execution= '+execution1
        r = s.get(url)  # 已经是登录状态了
        print '>>>>>>返回登录状态'
        if r.status_code==200:#获取返回状态
            print ">>>>>>登录成功"
        else:
            print ">>>>>>登录失败"
            #渠道助手添加客户页面
            s.get("http://crm.dev.great-tao.com/channel/customer/add")
            #供应商客户名称
        company='Calderon and Knapp Co'+str(random.randint(0, 999999))
        #companyEn名称
        companyEn = 'Calderon' + str(random.randint(0, 999999))
        # 添加供应商客户
        addgys = s.post(urlgys,data={
            'address':'Dolorem nihil aliquip blanditiis dicta',
            'breach':'1',
            'channelCustomerAttachments[0].uri':'https://image-dev.egtcp.com/2018/08/07/45d622e40c9a7109b8fcff56d7b96ae7.jpg',
            'city':'430900',
            'company':company,

            'companyContent':'Animi ratione soluta magna et dolorem numquam ',
            'companyEn':companyEn,
            'country':'-- 请选择 --',
            'customerRequirements':'4',
            'district':'430923',
            'employeesTotal':''+str(random.randint(0,4)),#员工数量
            'enterpriseType':'2',
            'industry':'3',
            'province':'430000',
            'requirementRemark':'Laudantium facilis sed similique maiores velit ',
            'role':'2',
            'setUpTime':'2018',
            'test':'3',
            'type':'8'
        })
        if addgys.status_code==200:
            print ">>>>>>供应商客户添加成功"
        else:
            print ">>>>>>供应商客户添加失败"


        # 打开数据库连接
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
        sql = "SELECT id FROM channel_customer WHERE company=%s"
        # 执行sql
        cursor.execute(sql,[company])

        results = cursor.fetchall()

        for x in results:
            print x['id']
        print results
        print x['id']
        # 提交，不然无法保存新建或者修改的数据
        s = results

        conn.commit()

        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()




if __name__ == '__main__':
    #构造测试集
    # suite = unittest.TestSuite()
    # suite.addTest(ApiDemoTest("Boss_test"))
    #执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()