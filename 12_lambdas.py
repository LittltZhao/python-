# -*- coding:utf-8 -*-
#lambda for-else

add=lambda x,y:x+y
print add(3,4)

a=[(1,2),(4,1),(9,10),(14,-1)]
print a
a.sort(key=lambda x:x[1])
print a

b1=[11,23,6,2]
b=[1,3,5,6]
data=zip(b1,b)
print
print data
data.sort()
print data
#列表并行排序
list1,list2=map(lambda t:list(t),zip(*data))
print list1
print list2

# for - els
for n in range(2,10):
    for x in range(2,n):
        if n%x ==0:
            print n,"=",x,"*",n/x
            break
    else:
        print n,"是个质数"


# 协程  数据的消费者
def greps(pattern):
    print "searching for",pattern
    while True:
        line=yield#协程会消费掉发送给它的值
        if pattern in line:
            print line

search=greps('love')
next(search) #next:启动协程
search.send('I love you') #send方法向yield传值
search.send("Don't you love me?")
search.send("No!")
search.close() #:关闭协程


# 函数缓存 Function caching
# 当一个I/O密集的函数被频繁使用相同的参数调用的时候,函数缓存可以节约时间。

from functools import wraps
def memoize(function):
    memo={}
    @wraps(function)
    def wrapper(*args):
        if args in memo:
            return memo[args]
        else:
            rv=function(*args)
            memo[args]=rv
            return rv
    return wrapper

@ memoize
def fib(n):
    if n<2:
        return n
    return fib(n-1)+fib(n-2)

print fib(25)

