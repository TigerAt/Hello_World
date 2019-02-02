#!/usr/bin/env python
#_*_coding:utf-8_*_
#Author:Tiger At
import paramiko

#读取私钥
private_key = paramiko.RSAKey.from_private_key_file('/home/xx/.ssh/id_rsa')

#创建SSH客户端
ssh = paramiko.SSHClient()

#允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#建立连接
ssh.connect('x.x.x.x',22,'xxxx',pkey=private_key)

#执行命令
stdin, stdout, stderr = ssh.exec_command("ifconfig")

#获取结果
data = stdout.read()
print(data.decode())
print(stderr.read().decode())
ssh.close()

