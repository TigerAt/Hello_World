#!/usr/bin/env python
#_*_coding:utf-8_*_
#Author:Tiger At
import paramiko

#创建SSH对象
ssh = paramiko.SSHClient()
#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#连接服务器
ssh.connect(hostname='x.x.x.x',port=22,username='xxx',password='xxxx')

#执行命令，stdin表示标准输入，stdout表示标准输出，stderr表示执行error
stdin, stdout, stderr = ssh.exec_command("ifconfig")

#获取命令结果
data = stdout.read()
#输出结果
print(data.decode())
#输出error
print(stderr.read().decode())

#关闭连接
ssh.close()

