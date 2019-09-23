#!/usr/bin/env python2.7
#coding=utf-8

import getpass

while True:
    pwd = int(getpass.getpass("猜数字游戏，请输入（1-100）："))
    if 1 <= pwd <= 100:
        break
    print "\n"

for i in range(1,11):
    print "\n"
#   num = int(input("第"+str(i)+"次猜测：") )
    num = int(input(("第%s次猜测：") % i) )
    if num > pwd:
        print "你猜的数字太【大】了，请重猜"
#       continue
    elif num < pwd:
        print "你猜的数字太【小】了，请重猜"
#       continue
    else:
        print "="*30
        print "恭喜你！第"+str(i)+"次猜对了!!"
        print "恭喜你！第%s次猜对了!!" % i
        print "="*30
        break
    i += 1
else:
    print "="*50
    print "很遗憾！8次机会没有猜到设定的数字(%s)，游戏结束！" % pwd
    print "很遗憾！8次机会没有猜到设定的数字(%s)，游戏结束！" % pwd
    print "="*50
