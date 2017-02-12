# -*- coding:utf-8 -*-
# 三元运算符

def test1():
    is_fat=True
    state='Fat' if is_fat else 'Not fat'
    return state

def test2():
    fat=True #Tru等同与1,False等同与0
    fitness=('skinny','fat')[fat]
    return fitness
print test2()
