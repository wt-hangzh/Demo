#!/usr/bin/env python2.7
#coding=utf-8

from __future__ import print_function 

for i in range(1,10):
    for j in  range(1,11):
        if  i >= j:
            plus = i + j
            print ('%-2s''+ ''%-2s''= ''%-2s' %(i,j,plus),end = ' ')
            j += 1
        else:
            print ('\n')
            break
    i += 1
