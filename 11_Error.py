# -*- coding:utf-8 -*-

def err():#单个异常
    try:
        files=open('test.txt','rb')
    except IOError as e:
        print "{}".format(e.args[-1])
def err1():#处理多异常
    try:
        files=open('test.txt','rb')
    except (IOError,EOFError) as e:#可能发生的异常放到元组
        print "{}".format(e.args[-1])
def err2():
    try:
        files=open('test.txt','rb')
    except EOFError as e:#可能发生的异常放到元组
        print "EOFEror"
        raise e #引发异常
    except IOError as e:
        print "error"
        raise e
    except Exception:
        raise

# finally从句中的代码不管异常是否触发都将会被执行
def err3():
    try:
        files=open('test.txt','rb')
    except IOError as e:
        print "{}".format(e.args[-1])
    finally:
        print "善后处理"

# try-else 从句：未出发异常时执行
def err4():
    try:
        #files=open('test.txt','rb')
        print "try"
    except Exception:
        print "exception"
    else:
        print "else"
    finally:
        print "finally"
    
