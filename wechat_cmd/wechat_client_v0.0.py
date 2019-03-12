#!/usr/bin/env python
#_*_coding:utf-8_*_
#Author:Tiger At
import threading
import time
import itchat

#用于保存最近联系人
recent_frends = []
#用于显示功能项
features = ('好友列表', '新会话', '最近会话')


# itchat固定语法，打印交互信息
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    print((time.strftime('%Y-%m-%d %H:%M:%S ')+"\033[31;1m%s\033[0m: \n" + msg['Text']) % (msg['User']['RemarkName']))

#获取最近联系人信息
def get_recent_friend():
    # 判断recent_friends 列表是否为空，如果不为空则打印最近联系人RemarkName
    while recent_frends:
        recent_frends_obj = recent_frends.pop()
        print(recent_frends_obj[0]['RemarkName'],end='\t')

# 获取全部好友
def get_friend():
    friends = itchat.get_friends(update=True)
#显示好友信息，每次打印10位好友信息，输入end结束显示
    num = 0
    for friend in friends:
        if num == 10:
            num = 0
            show_buttons = input('\n继续请输入任意字符，结束显示返回主界面输入【end】:')
            if show_buttons == 'end':
                break
            else:
                print(friend['RemarkName'] or friend['NickName'],end='\t')
        else:
            print(friend['RemarkName'] or friend['NickName'], end='\t')
            num+=1
    print('已自动跳转至主界面')

#发送信息
def send_message():
    global recent_frends
    while True:
        friend = input('请输入好友昵称(【end】返回主界面)：')
        if friend == 'end':
            break
        elif friend=='':
            continue
        else:
            # 获取好友信息
            users = itchat.search_friends(name=u'%s' % friend)
            if users:
                if users in recent_frends:
                    pass
                else:
                    recent_frends.append(users)
                print("开始与【\033[31;1m%s\033[0m】对话(【exit】结束本次对话)"%users[0]['RemarkName'])
                # 获取`UserName`,用于发送消息
                userName = users[0]['UserName']
                while True:

                    input_message = input(time.strftime('%Y-%m-%d %H:%M:%S ')+'Me with \033[31;1m%s\033[0m:\n'%users[0]['RemarkName'] )
                    if input_message == 'exit':
                        print("结束与【\033[31;1m%s\033[0m】对话"%users[0]['RemarkName'])
                        break
                    else:
                        itchat.send(str(input_message), toUserName=userName)
            elif friend == '':
                continue
            else:
                print("通讯录无此人")


if __name__ == '__main__':
    itchat.auto_login(hotReload=True) #微信登录接口 itchat.auto_login(enableCmdQR=True)用于显示二维码
    t2 = threading.Thread(target=itchat.run) #定义线程2用于显示好友信息
    t2.setDaemon(True) #设置线程2为守护线程，在主线程结束后自动结束
    t2.start() #启动线程2
    while True:
        for i,j in enumerate(features):
            print(i,j,)
        feature_id=input("请输入功能编号(【q】退出程序):")
        if feature_id == 'q':
            print("see you again")
            break
        elif feature_id.isdigit():
            feature_id = int(feature_id)
            if feature_id ==0:
                get_friend()
            elif feature_id ==1:
                t1 = threading.Thread(target=send_message)
                t1.start()
                t1.join()
            elif feature_id ==2:
                get_recent_friend()






