#!/usr/bin/env python
#_*_coding:utf-8_*_
#Author:Tiger At
#此代码用于“糗事百科相关”一定页码范围的html页面抓取，仅供娱乐和学习

#导入requests模块用于进行数据爬取，os模块用于创建文件夹
import requests,os

#此字典用于存储“糗事百科”中相关版块按钮信息
sections = {
    "热门":'8hr',
    "24小时":'hot',
    "热图":'imgrank',
    "文字":'text',
    "穿越":'history',
    "糗图":'pic',
    "新鲜":'textnew'
}

#此方法用于显示版块信息
def show_section():
    for i in sections:
        print(i,end='\t') #以制表符结尾 方便版块信息的横向显示


#此方法用于根据用户所输入的信息进行相关版块url的提取及文件夹的创建
def handle_input():
    while True:
        show_section()
        section = input("\n请输入所要爬取的版块信息（退出q）:")
        if section == 'q':
            return 'q'

        # 判断用户输入的信息是否存在相关版块内，如果存在则进行后续操作
        elif section in sections:
            # 获取当前程序所在路径,还有一种方式是直接写当前目录无需获取但会偶发性报错（'./文件夹名称'）不建议使用
            current_path = os.path.abspath('.')
            # 在当前程序文件所在目录下创建新目录：
            conf_dir = os.path.join(current_path, section)  # 构造新的路径
            if not os.path.exists(conf_dir):  # 判断目录是否存在，如果不存在则创建
                os.mkdir(conf_dir)  # 创建目录
            url = 'https://www.qiushibaike.com/%s/' % (sections[section])
            return url,section

#此方法用于数据的抓取
def grab(url,section):
    #用户输入抓取的起始页码
    start_num = int(input("请输入要抓取的起始页码："))
    end_num = int(input("请输入要抓取的起始页码："))
    #自定义UA请求头信息
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    # 获取响应中的页面数据
    for i in range(start_num,end_num+1):
        print(url + 'page/%s/' % str(i))
        #发送请求
        response = requests.get(url = url + 'page/%s/' % str(i),headers = headers)
        #获取数据
        page_text = response.text
        #指定文件路径（即handle_input()所创建的目录下）
        file_path = './%s/' % section + str(i) + '.html'

        #进行数据的持久化存储
        with open(file_path,'w',encoding='utf-8') as fb:
            fb.write(page_text)
            print("第%d页写入数据完成")


if __name__ == '__main__':
    url,section = handle_input()
    if url == 'q':
        exit()
    else:
        grab(url,section)

