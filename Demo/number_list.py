#!/usr/bin/env python2.7
#coding=utf-8

from __future__ import print_function 

j = 1

for i in range(1,101):
    if j % 10 == 0:
        print ('%-4s' % i,end = '\n')
    else:
        print ('%-4s' % i,end = ' ')
    i += 1
    j += 1
