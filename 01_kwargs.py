# -*- coding:utf-8 -*-
import pdb
def test_args(f,*argv):#*args用于发送一个非键值对的可变数量的参数列表给一个函数
    print "first arg: ",f
    for arg in argv:
        print "another arg :",arg
# test_args("yas",'python','eggs','test')


# **kwargs 允许将不定长度的键值对，作为参数传给函数
def greet_test(**kwargs):
    for key,value in kwargs.items():
        print "{0}=={1}".format(key,value)
# greet_test(name=1)


def test_args_kwargs(arg1,arg2,arg3):
    pdb.set_trace()#pdb调试代码 设置断点
    """
    c:继续执行
    w:显示当前正在执行代码的上下文信息
    a:打印当前函数的参数列表
    s:执行当前代码行，并停在第一个能停的地方
    n:继续执行到当前函数的下一行，或者当前行直接返回
    """
    print "arg1:",arg1
    print "arg2:",arg2
    print "arg3:",arg3
args=("twr",3,5)
test_args_kwargs(*args)

kwargs={"arg3":1,"arg2":2,"arg1":3}
test_args_kwargs(**kwargs) #只取了值没有取键(对该函数来说)
