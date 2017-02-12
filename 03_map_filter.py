# -*- coding:utf-8 -*-
# map将一个函数映射到一个输入列表的所有元素上

def test_map():#应用于普通list
    items=[1,2,3,4,5]
    squared=list(map(lambda x:x**2,items))#对每个元素都进行函数操作
    return squared

def test_map2():#应用于函数list
    def mul(x):
        return x*x
    def add(x):
        return x+x
    funs=[mul,add]
    for i in range(5):
        value=list(map(lambda x:x(i),funs))
        print value

# print test_map2()


# filter 创建一个列表,其中每个元素都是对一个函数能返回True.
def test_filter():
    nums=range(-5,5)
    less_than_zero=list(filter(lambda x:x<0,nums))
    return less_than_zero
print test_filter()

