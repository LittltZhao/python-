# -*- coding:utf-8 -*-
# 推导式 解析式

# 列表解析
multiples=[x for x in range(30) if x%3==0]
print multiples
squred=[x**2 for x in range(5)]
print squred

#字典推导
mcase={'a':10,'b':34,'A':7,'Z':3}
mcase_fre={
    k.lower():mcase.get(k.lower(),0)+mcase.get(k.upper(),0)#统计大小写的总次数
    for k in mcase.keys()}
print mcase_fre
print mcase
print {v:k for k,v in mcase.items()}#对换字典的键和值

#集合推导
squred1={x**2 for x in [1,3,1,5]}
print squred1
