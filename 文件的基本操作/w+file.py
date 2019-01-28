#!/usr/bin/env python
#_*_coding:utf-8_*_
#Author:Tiger At

f = open("test.txt",'w+',encoding='utf-8')
print(f.read())
for i in range(1,5):
    f.write("\n第%s次写入"% i)

print(f.read())

f.close()

