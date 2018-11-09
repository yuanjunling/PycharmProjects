#coding=utf-8
import requests
import re
import unittest
import pymysql
import json
import random,time,sys


class ApiBossTest(unittest.TestCase):
    # 供应商客户名称
    global company
    company = 'Calderon and Knapp Co' + str(random.randint(0, 999999))
    global s
    s = requests.Session()  # 保持Cookie
    def setUp(self):
        self.log = 'https://cas.dev.great-tao.com/cas-server/login?service=http://boss.dev.great-tao.com/cas'
        self.url = 'http://boss.dev.great-tao.com/index'
        self.urladd = 'http://crm.dev.great-tao.com/channel/customer/save'


    def test_Boss_log(self):
        log_url = self.log
        url = self.url
        a1 = s.get(log_url).content  # 获取页面源码
        lt1 = re.search('name="lt" value="(.*)" />', a1).group(1)  # 查找源码中的lt
        execution1 = re.search('name="execution" value="(.*)" ', a1).group(1)

        # 登录BOSS系统
        s.post(log_url, data={'username': 'yuanjunling',
                                'password': '1234',
                                'captcha': 'greattao0818',
                                'submit': 'LOGIN',
                                '_eventId': 'submit',
                                'lt': lt1,
                                'execution': execution1},
               )  # POST帐号和密码，设置headers

        print 'lt= ' + lt1
        print 'execution= ' + execution1
        r = s.get(url)  # 已经是登录状态了
        print '>>>>>>返回登录状态'
        if r.status_code == 200:  # 获取返回状态
            print ">>>>>>登录成功"
        else:
            print ">>>>>>登录失败"


        self.assertEqual(r.status_code,200) #断言html状态码
    def test_addSuppliers(self):
        global urladd1
        urladd1 = self.urladd
        #渠道助手添加页面
        s.get(urladd1)

        # companyEn名称
        companyEn = 'Calderon' + str(random.randint(0, 999999))
        # 添加供应商客户
        addgys = s.post(urladd1, data={
            'address': 'Dolorem nihil aliquip blanditiis dicta',
            'breach': '1',
            'channelCustomerAttachments[0].uri': 'https://image-dev.egtcp.com/2018/08/07/45d622e40c9a7109b8fcff56d7b96ae7.jpg',
            'city': '450200',
            'company': company,

            'companyContent': 'Animi ratione soluta magna et dolorem numquam ',
            'companyEn': companyEn,
            'country': '-- 请选择 --',
            'customerRequirements': '4',
            'district': '450205',
            'employeesTotal': '' + str(random.randint(0, 4)),  # 员工数量
            'enterpriseType': '2',
            'industry': '3',
            'province': '450000',
            'requirementRemark': 'Laudantium facilis sed similique maiores velit ',
            'role': '2',
            'setUpTime': '2018',
            'test': '3',
            'type': '8'
        })
        if addgys.status_code == 200:
            print ">>>>>>供应商客户添加成功"
        else:
            print ">>>>>>供应商客户添加失败"

        sql = "SELECT id FROM channel_customer WHERE company=%s"

        #调用数据库查询company的id
        resultObj = test_sql(sql, company)
        for x in resultObj:
            print x['id']
        a2 = x['id']
        print a2
    def test_addprocurer(self):
        s.get(urladd1)
        company2 = 'Ayala and Carroll Associates' + str(random.randint(0, 999999))
        companyEn2 = 'Carpenter Reilly Plc' + str(random.randint(0, 999999))
        #添加采购商
        addcgs = s.post(urladd1, data={
            'address': 'Dolorem nihil aliquip blanditiis dicta',
            'breach': '0',
            'channelCustomerAttachments[0].title':'name',
            'channelCustomerAttachments[0].uri': 'https://image-dev.egtcp.com/2018/08/07/45d622e40c9a7109b8fcff56d7b96ae7.jpg',
            'company': company2,
            'companyContent': 'Animi ratione soluta magna et dolorem numquam ',
            'companyEn': companyEn2,
            'country': 'BG',
            'customerRequirements': '2',
            'employeesTotal': '' + str(random.randint(0, 4)),  # 员工数量
            'enterpriseType': '0',
            'industry': '6',
            'requirementRemark': 'Laudantium facilis sed similique maiores velit ',
            'role': '1',
            'setUpTime': '2018',
            'test': '6',
            'type': '1'
        })
        if addcgs.status_code==200:
            print "采购商添加成功"
        else:
            print "采购商添加失败"


#数据库函数
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
