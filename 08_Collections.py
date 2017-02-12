# -*- coding:utf-8 -*-
# 容器 collections

# defaultdic 不需要检查key是否存在
from collections import defaultdict
colors=(
    ('Yasoob','Yellow'),
    ('Ali','Blue'),
    ('Arham','Green'),
    ('Ali','Black'),
    ('Yasoob','Red'),
    ('Ahmed','Silver'),
)
favorite_color=defaultdict(list)

for name,color in colors:
    favorite_color[name].append(color)
print favorite_color
print

#当你在一个字典中对一个键进行嵌套赋值时,如果这个键不存在,会触发keyError异常
tree=lambda:defaultdict(tree)
some_dict=tree()
some_dict['colors']['favorite']='Yellow'
import json
print some_dict
print json.dumps(some_dict)
print

#Counter计数器
from collections import Counter
favs=Counter(color for name,color in colors)
print favs
#统计文件行数
def coun(filename):
    with open(filename,'rb') as f:
        linecount=Counter(f)
    return linecount
print 
#deque 双端队列
# 从头/尾两端添加或删除元素
from collections import deque
d=deque()
d.append('1')
d.append('2')
d.append('3')
print len(d)
print d[0]
print d
print d.popleft()#左弹出
print d.pop()#右弹出
print d
d.extendleft([0])#左扩展
d.extend([6,7,8])#右扩展
print d
print
#限制这个列表的大小,当超出你设定的限制时,数据会从对队列另一端被挤出去(pop)


# namedtuple 命名元组 用字典访问的方式访问元组的元素
# 把元组变成一个针对简单任务的容器
from collections import namedtuple
Animal=namedtuple('A1nimal','name age type')#两个参数:元组名称和字段名称
perry=Animal(name='perry',age=31,type='cat')
print perry
print perry.name,perry.age,perry.type
print perry[0]
# perry.name='jo' 不可修改
print perry._asdict()['age']#将元组转化为字典
print 


# Enum 枚举
from enum import Enum
from collections import namedtuple

class Species(Enum):
    cat=1
    dog=2
    horse=3
    owl=4
drogon=Animal(name='dog',age=2,type=Species.dog)
print drogon
print drogon.type
print 




#enumerate 枚举
my_list=['apple','banana','grape','pear']
for c,value in enumerate(my_list,1):#1表示从哪个数字开始枚举
    print c,value
for c,value in enumerate(my_list):
    print c,value
#创建包含索引的元组列表
counter_list=list(enumerate(my_list))
print counter_list


