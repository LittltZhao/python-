# -*- coding:utf-8 -*-
# 上下文管理器 with 确保我们的文件会被关闭,而不用关注嵌套代码如何退出
# 上下文管理器的一个常见用例,是资源的加锁和解锁,以及关闭已打开的文件

# 基于类的实现 一个上下文管理器的类,最起码要定义__enter__和__exit__方法
class File():
    def __init__(self,file_name,file_mod):
        self.file_obj=open(file_name,file_mod)
    def __enter__(self):
        return self.file_obj

    # __exit__接受三个必须的参数 过程如下：
    # (1)with语句暂存零File类的__exit__方法
    # (2) 然后调用File的__enter__方法
    # (3)__enter__方法打开文件并返回给with语句
    # (4)打开文件的句柄被传递给opened_file参数
    # (5)适用.write()来写文件
    # (6)with 语句调用之前暂存的__exit__方法
    # (7)__exit__方法关闭文件
    def __exit__(self,type,value,traceback):
        self.file_obj.close()

# 定义__enter__和__exit__方法,我们可以在with语句里使用它
with File('c.txt','w') as opened_file:
    opened_file.write('hola!')

# 处理异常 __exit__
# __exit__的三个参数:type,value,traceback
# 第四步和第六步之间发生异常，则将异常的type,value,traceback传递到__exit__方法
class FF():
    def __init__(self,file_name,file_mod):
        self.file_obj=open(file_name,file_mod)
    def __enter__(self):
        return self.file_obj
    def __exit__(self,type,value,traceback):
        print "Exception has been handled"
        self.file_obj.close()
        return True #return True不抛出异常，返回其他的with语句抛出异常
with FF('func2.log','w') as opened_file1:
    opened_file1.undefined_function()


#基于生成器的上下文管理器
from contextlib import contextmanager

@ contextmanager
def open_file(name):
    f=open(name,'w')
    yield f
    f.close()
with open_file('c.txt') as f:
    f.write('abc')

