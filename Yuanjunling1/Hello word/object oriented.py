#coding=utf-8
# class Employee:
#     '所以员工的基类'
#     empCount = 0
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#         Employee.empCount +=1
#     def displayCount(self):
#         print "Total Employee %d " % Employee.empCount
#     def displayEmployee(self):
#         print "name : ",self.name,", Salary: ",self.salary




# class Test:
#     def prt(runoob):
#         print(runoob)
#         print(runoob.__class__)
#
#
# t = Test()
# t.prt()
# "创建 Employee 类的第一个对象"
# emp1 = Employee("yuan",3000)
# "创建 Employee 类的第二个对象"
# emp2 = Employee("jun",5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print "Total Employee %d" % Employee.empCount
# emp1.age = 9
# print hasattr(emp1,'age') # 如果存在 'age' 属性返回 True。
# del emp2.name #删除name属性
# print hasattr(emp2,'name')
# print Employee.__doc__
# print Employee.__name__
#
# class Child(Employee):
#     def __init__(self):
#         print "调用子类构造方法"





class Parent:  # 定义父类
    parentAttr = 0

    def __init__(self):
        print "调用父类构造函数"

    def parentMethod(self):
        print '调用父类方法'

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print "父类属性 :", Parent.parentAttr


class Child(Parent):  # 定义子类
    def __init__(self):
        print "调用子类构造方法"

    def childMethod(self):
        print '调用子类方法'


c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(300)       # 再次调用父类的方法 - 设置属性值
c.getAttr()          # 再次调用父类的方法 - 获取属性值