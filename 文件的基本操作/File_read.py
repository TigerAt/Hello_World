#!/usr/bin/env python
#_*_coding:utf-8_*_
#Author:Tiger At
import chardet
#读取文件
#solution 1 全部取出文件内容
f = open(file=r"E:\Study\Python\PycharmProjects\Hello_World\SecureCRT Session\Test\old_session\x.x.x.x.ini",mode='r',encoding='utf-8')
data = f.read()
f.close()
'''
print(chardet.detect(data))
data=data.decode("utf-8")
print(data)
'''
#solution 2 逐行取出 解决文件大读取慢的问题
f = open(file=r"E:\Study\Python\PycharmProjects\Hello_World\SecureCRT Session\Test\old_session\x.x.x.x.ini",mode='r',encoding='utf-8')
#我们常用’/‘来表示相对路径，’\‘来表示绝对路径，上面的路径里\\是转义的意思，如果不想用\\转移，那及在路径前面添加‘r’转移字符
for line in f:
    print(line)  #此处读出的文件默认有'/n',因为print读取结束自动添加换行符，而line.strip()就可以去除换行符
f.close()