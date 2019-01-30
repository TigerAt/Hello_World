1.此脚本用于批量创建SecureCRT Session使用，python版本为:V3.7.0
2.脚本测试的SecureCRT的版本为:V8.5.0，其他版本尚未测试
3.“config”目录下的‘ip.txt’文件用户可根据自己的实际需求进行IP信息的更改，'ssh_template.ini'文件为初始的ssh配置
模板文件，'telnet_template.ini'文件为初始的telnet配置模板文件，是通过SecureCRT自动生成的配置文件，如若想自定义其
它配置文件，可用CRT自动生成一个的初始配置文件，并将文件中“Hostname”修改为“x.x.x.x”,文件重命名为对应登录方式
配置模板即可。
4.使用python直接运行'main.py'即可，运行结果是在'main.py'所在目录下创建自定义的Session目录，并在这个session目录下
创建完成SecureCRT的配置文件，创建完成后可直接将自定义的这个目录直接copy至SecureCRT的Session目录下即可

注：此脚本的基本原理为根据已有的CRT配置文件，修改文件中的“Hostname”字段信息，完成其它配置文件的生成，最主要为
文件的相关操作。此脚本为初始版本V0.0 后续将根据实际情况进行代码的更新，敬请关注


