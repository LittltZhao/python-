# -*- coding:utf-8 -*-
# 装饰器是修改其他函数的功能的函数

# def hi(name="dsaf"):
#    return "hi "+name

# print hi()
# greet=hi#没有小括号,函数赋值给变量
# print greet()

# del hi#删除hi旧函数
# print greet()#不受影响
# print hi()#error



# 函数中定义函数 函数嵌套
def hi1(name='yasoob'):
    print "hi()"
    def greet():
        return "greet()"
    def welcome():
        return "welcome()"
    print greet()
    print welcome()
    print "hi()"
# hi1()
# greet()#错误


# 从函数中返回函数
def hi3(name='jyas'):
    def greet():
        return "greet()"
    def welcome():
        return "welcome()"
    if name=='jyas':
        return greet #输出函数变量，而表示函数结果
    else:
        return welcome
#a=hi3()
#print a #a指向greet的地址，故返回地址
#print a() #执行函数
#print hi3('abc')() #两个括号,执行结果

# 将函数作为参数传递给另一个函数
def hi4():
    return "hi yasoob!"

def dosome(func):#函数作参数
    print "before hi()"
    print func#返回地址
    print func()#返回函数执行结果

# dosome(hi4)



# 装饰器让你在一个函数的前后去执行代码
def a_decorator(func):# 封装一个函数,并且用这样或者那样的方式来修改它的行为
    def wrapTheFunction():
        print "before func()"
        func()
        print "after func()"
    return wrapTheFunction
def a_function_decorator():
    print "functions require decorators"

# a_function_decorator()
# a_function_decorator=a_decorator(a_function_decorator)
# a_function_decorator()

@ a_decorator #使用@更简单地调用装饰器
def a_function_requiring_decoration():
    print "functions require decorators @"

a_function_requiring_decoration()
print a_function_requiring_decoration.__name__
#函数名被wrapTheFunction替代，重写了我们函数的名字和注释文档



# functools.wraps解决函数名和文档被修改问题
from functools import wraps
# @wraps接受一个函数来进行装饰,并加入了复制函数名称、注释文档、参数列表
# 等等的功能。这可以让我们在装饰器里面访问在装饰之前的函数的属性
def a_new_decorator(func):
    @wraps(func)#防止被修饰函数的函数名和注释被修改
    def wrapTheFunction():
        print "before func()"
        func()
        print "after func()"
    return wrapTheFunction#无括号

@a_new_decorator
def functions():
    print "functions @wrap"
print
print functions.__name__#返回函数名





def decorator_name(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        if not can_run:
            return "Function will not Run"
        return f(*args,**kwargs)
    return decorated
@decorator_name
def func():
    return "Function is Runing"

can_run=True
print func()
can_run=False
print func()




# 授权 装饰器能有助于检查某个人是否被授权去使用一个web应用的端点(endpoint)
def requires_auth(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        auth=request.authorization
        if not auth or not check_auth(auth.username,auth.password):
            authenticate()
        return f(*args,**kwargs)
    return decorated

# 日志
def logit(func):
    @wraps(func)
    def with_loggint(*args,**kwargs):
        print func.__name__+"was called"
        return func(*args,**kwargs)
    return with_loggint
@logit
def addition_func(x):
    return x+x
print
print addition_func(4)
print

#带参数的装饰器
def logit1(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args,**kwargs):
            log_string=func.__name__
            print log_string
            with open(logfile,'a') as opened_file:
                opened_file.write(log_string+'\n')
        return wrapped_function
    return logging_decorator
@logit1()
def myfunc1():
    pass
myfunc1()

@logit1(logfile='func2.log')
def myfunc2():
    pass
myfunc2()


# 装饰器类
class logit2(object):
    def __init__(self,logfile='out2.log'):
        self.logfile=logfile

    def __call__(self,func):
        log_string=func.__name__+" was called"
        print log_string
        with open(self.logfile,'a') as opened:
            opened.write(log_string+'\n')
        self.notify()#发送一个通知
    def notify(self):
        pass 
@logit2()
def myfunc4():
    pass

# email子类
class email_logit(logit2):
    def __init__(self,email='admin@myproject.com',*args,**kwargs):
        self.email=email
        super(logit2,self).__init__(*args,**kwargs)
    def notify(self):
        # 发送邮件的实现
        pass

