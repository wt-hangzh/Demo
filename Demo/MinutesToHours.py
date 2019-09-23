#!/usr/bin/env python2.7
#coding=utf-8

import sys
def Hours(m):
    if int(m) < 0:
        raise ValueError("value error!")
    else:
        print("%s H,%s M" %(int(m) // 60,int(m) % 60))

if __name__ == '__main__':
    while 1:
        try:
            Hours(sys.argv[1])
            break
        except ValueError:
            print("Parameter Error")
            break

"""
import sys

# 转换函数
def Hours(minute):
    # 如果为负数则 raise 异常
    if minute < 0:
        raise ValueError("Input number cannot be negative")
    else:
        print("{} H, {} M".format(int(minute / 60), minute % 60))

# 函数调用及异常处理逻辑
try:
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")
"""
