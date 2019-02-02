#!/usr/bin/env python
#_*_coding:utf-8_*_
#Author:Tiger At
import paramiko

private_key = paramiko.RSAKey.from_private_key_file('/home/xx/.ssh/id_rsa')
transport = paramiko.Transport(('x.x.x.x',22))
transport.connect(username='xxxx',pkey=private_key)

sftp = paramiko.SFTPClient.from_transport(transport)

#sftp.put('ssh_sftp.py','/home/xxx/workstation/project/company/ssh_sftp.py')
sftp.get('/home/xxx/workstation/project/company/test.txt','heh.txt')

transport.close()