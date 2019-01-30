#!/usr/bin/env python
#_*_coding:utf-8_*_
#Author:Tiger At
import os
ip_list=[] #定义存放IP地址的列表


def read_ip(ip_file_name): #此方法用来读取存放IP地址的文件
    global ip_list
    ip_file = open(ip_file_name,'r')
    for line in ip_file:
        ip_list.append(line.split()) #将读取的IP地址存入ip_list列表
    ip_file.close()

def create_conf_file(init_file,conf_file_name,ip): #此方法用来创建新的配置文件
    #定义配置文件模板
    f_name = init_file
    old_str = "x.x.x.x" #此处的字符串与CRT生成的配置文件的Hostname所对应的值一致

    f_file = open(f_name, 'r')
    f_new = open(conf_file_name, 'w')
    for line in f_file:
        if old_str in line: #在配置文件中进行设备管理IP地址的写入
            line = line.replace(old_str, ip)
        f_new.write(line) #其他内容逐行写入
    f_file.close()
    f_new.close()

if __name__ == "__main__":
    Floder_name = input("请输入配置文件所在文件夹的名称:") #自定义保存配置的目录名称
    while True:
        Login_type = input("请输入登录方式（SSH/TELNET）:") #选择配置文件的登录方式
        if Login_type == 'SSH': #选择SSH方式登录
            init_file = 'config/ssh_template.ini' #此处的模板文件时我通过CRT自动生成的模板文件，可根据实际情况进行文件替换
            break
        elif Login_type == 'TELNET': #选择TELNET方式登录
            init_file = 'config/telnet_template.ini' #此处的模板文件时我通过CRT自动生成的模板文件，可根据实际情况进行文件替换
            break
        else:
            print("输入有误.....")
            continue
    current_path = os.path.abspath('.') #获取当前程序所在路径
    #在当前程序文件所在目录下创建新目录：
    conf_dir = os.path.join(current_path,Floder_name)  #构造新的路径
    if not os.path.exists(conf_dir): #判断目录是否存在，如果不存在则创建
        os.mkdir(conf_dir)  #创建目录
    else:
        pass
    # 读取“ip.txt”文件
    read_ip("config/ip.txt")

    #创建配置文件
    for i,j in enumerate(ip_list):
        s = ''.join(j)
        conf_file_name = "%s\%s.ini" % (conf_dir,s)
        create_conf_file(init_file,conf_file_name,s)
    print("配置文件创建完毕，请将%s文件夹拷贝至CRT的session目录下" % Floder_name)

