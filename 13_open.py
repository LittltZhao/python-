# -*- coding:utf-8 -*-

with open('c.txt','r+') as f:
    # r:读
    # r+: 读取并写入
    # w : 写入
    # a : 末尾添加
    files=f.read()

import io#指定编码
with io.open("c.txt",'w',encoding="utf-8") as f:
    f.write(u'abc\n')
