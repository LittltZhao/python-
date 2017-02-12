# -*- coding:utf-8 -*-
#global变量意味着我们可以在函数以外的区域都能访问这个变量
def add(a,b):
    global result# 尽量避免使用global
    #没有global时，result变量只能在创建它的函数内部才允许访问
    result=a+b
add(2,4)
print result


#通过global返回多个变量
def profile():
    global name
    global age
    name='Danny'
    age=30
profile()
print name
print age

#tuple 返回多个变量
def profile1():
    name1="danny"
    age=31
    return (name1,age)
    #return name1,age
pro=profile1()
print pro[0],pro[1]



#对象变动Mutation
#将一个变量赋值为另一个可变类型的变量时,对这个数据的任意改动会同时反映到这两个变量上去（只针对可变数据类型)
def add_to(num,target=[]):
    target.append(num)
    return target
print add_to(1)  #[1]
print add_to(2)  #[1,2]
print add_to(3)  #[1,2,3]
# 当函数被定义时,默认参数只会运算一次,而不是每次被调用时都会重新运算

def add_to1(num,target=None):#不要定义可变类型的默认参数
    if target is None:
        target=[]
    target.append(num)
    return target
print add_to1(1)
print add_to1(2)




# __slots__
# 默认情况下Python用一个字典来保存一个对象的实例属性
# 对于有着已知属性的小类来说,它可能是个瓶颈。这个字典浪费了很多内存。
# 使用__slots__来告诉Python不要使用字典,而且只给一个固定集合的属性分配空间
class MyClass(object):
    def __init__(self,name,dientifier):
        self.name=name
        self.identifier=identifier
        self.set_up()
#使用slots
class MyClass1(object):
    __slots__=['name','identifier']#类小的时候减小内存消耗
    def __init__(self,name,identifier):
        self.name=name
        self.identifier=identifier
        self.set_up()


# 虚拟环境 virtualenv
# pip install virtualenv
# virtualenv myproject
# source bin/activate
# deactivate
