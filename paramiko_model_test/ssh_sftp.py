#!/usr/bin/env python
#_*_coding:utf-8_*_
#Author:Tiger At
import paramiko

#封装transport
transport = paramiko.Transport(('x.x.x.x',22))
transport.connect(username='xx',password='xxxxx')

#启动sftpClient
sftp = paramiko.SFTPClient.from_transport(transport)

#将ssh_sftp_pub.py 上传至服务器 /home/xx/tigeratworkstation/ssh_sftp_pub.py
sftp.put('ssh_sftp_pub.py','/home/xx/tigeratworkstation/ssh_sftp_pub.py')
# 将/home/xxxx/workstation/project/company/test.txt 下载到本地 heh.txt
sftp.get('/home/xxxx/workstation/project/company/test.txt','heh.txt')

transport.close()