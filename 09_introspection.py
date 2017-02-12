# -*- coding:utf-8 -*-
# 自省(introspection),在计算机编程领域里,是指在运行时来判断一个对象的类型的能力

#dir()  返回一个列表,列出了一个对象所拥有的属性和方法
my_list=[1,2,4]
print dir(my_list)
print dir()#运行dir()而不传入参数,那么它会返回当前作用域的所有名字

#type 返回对象类型 id 返回任意不同种类对象的唯一ID
print type('')
print type([])
print type(dict)
print id(my_list)


# inspect模块
# 获取活跃对象的信息
import inspect
# 查看对象的成员
print inspect.getmembers(str)

