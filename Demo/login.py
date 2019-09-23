#!/usr/bin/env python2.7
#coding=utf-8

 
import datetime
today = datetime.date.today()
username = 'aaa'
password = '123'
count = 0
while count <3:
    uname = input('请输入用户名:')
    pwd = input('请输入密码:')
    if not uname.strip() or not pwd.strip():
        # print(uname)
        # print(pwd)
        print('用户名或密码不能为空')
    elif uname != 'aaa'or pwd != '123' :
        # print(type(uname))
        print('用户名或密码错误,请重新输入')
    else :
        welcome = '恭喜你登录成功了,欢迎%s 今天是%s '%(uname,today)
        print(welcome)
        break
    count+=1
else:
    print('错误次数超过3次,不允许登录')
 
 
 
