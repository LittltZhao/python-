# -*- coding:utf-8 -*-

def duplicate(some_list):#set 找到list中重复的元素
    dup=set([x for x in some_list if some_list.count(x)>1])
    return list(dup)

def duplicate2(some_list):#直接查找
    dup=[]
    for i in some_list:
        if some_list.count(i)>1:
            if i not in dup:
                dup.append(i)
    return dup
s=['a','b','c','d','e','b','m','n','n']

# print duplicate2(s)

def Intersection(valid,sets):#交集
    return sets.intersection(valid)
def Difference(valid,sets):#补集
    return sets.difference(valid)

valid=set(['a','b','c','d'])
sets={'a','b','e','f'}#直接创建set
print Intersection(valid,sets)
print Difference(valid,sets)
