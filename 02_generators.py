# -*- coding:utf-8 -*-
# 适用情况：不想同一时间将所有计算出来的大量结果集分配到内存当中
# 生成器也是一种迭代器,但是你只能对其迭代一次。这是因为他们并没有把所有的值存在内存中,而是在运行时生成值。
# 区分可迭代对象和迭代器对象:
# 一个迭代器是任意一个对象,只要它定义了一个next(Python2) 或者__next__方法
# 可迭代对象是Python中任意的对象,只要它定义了可以返回一个迭代器的__iter__方法,或者定义了可以支持下标索引的__getitem__方法
def generator():
    for i in range(3):
        yield i

# for i in generator():
    #print i
gen=generator()# gen为迭代器对象
print next(gen)#next()获取序列的下一个元素
print next(gen)
print next(gen)

#list str都是可迭代对象，但是不是迭代器对象
mystring='ysadfs'
myiter=iter(mystring)#iter()根据一个可迭代对象返回一个迭代器对象
print next(myiter)


#生成器占用更少的资源
def fibon(n):
    a=b=1
    for i in range(n):
        yield a
        a,b=b,a+b
#for x in fibon(100):
    #print x,

def fibon1(n):#list方式占用更多资源
    a=b=1
    result=[]
    for i in range(n):
        result.append(a)
        a,b=b,a+b
    return result




