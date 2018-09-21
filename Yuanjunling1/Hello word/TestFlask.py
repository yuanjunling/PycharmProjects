# -*- coding:utf-8 -*-
import time
import calendar
list1 = ['python','java','php','C++','C#']
list2 = ['jjj','ppp','lll','ddd']
print "list1[1]:",list1[1]
print list1+list2
list2.append('append')
print list2
del list2[3]
print list2*4
print len(list2)
list2.reverse()
print list2
tikce = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print "当前时间戳：", tikce
cal = calendar.month(2018,6)
print "以下输出2018年6月份的日历:"
print cal
#自定义函数
def printme(str):
    "打印任何传入的字符串"
    print str;
    return ;
#调用函数
printme("哈哈哈哈哈哈哈哈哈");
printme("我在调用一次啊");


#可写函数说明
def changeme(mylist):
    "修改传入的列表"
    mylist.append([1,2,3]);
    print "函数获取值：",mylist
    return
#调用changeme函数
mylist = [10,20,30];
changeme(mylist);
print "函数外取值: ", mylist

#可写函数说明
def printer(sta):
    print sta;
    return
printer(11111)
def printinfo(name,age):
    "打印任何传入的字符串"
    print "Name:",name;
    print "Age",age;
    return ;
#调用printinfo函数
printinfo(name="jun",age=222)
def functionname( arg1, *vartuple ):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return;


# 调用printinfo 函数
functionname(10)
functionname(10,20,30,40,50);
# 可写函数说明
sum = lambda arg1,arg2:arg1 + arg2;
# 调用sum函数
print "相加后的值为 : ", sum( 10, 20 )
print "相加后的值为 : ", sum( 20, 20 )
str1 = raw_input("请输入：")
print "你输入的内容是: ", str1

str2 = input("请输入：")
print "你输入的内容是：",str2;
fo = open("D:\\foo.txt","w")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
