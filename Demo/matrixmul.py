#!/usr/bin/env python2.7
#coding=utf-8

from __future__ import print_function

n = int(input('matrixmul A*B,please input level n = :'))
A = []
B = []
C = []

print ("please input matrix A:")
'''
for i in range(0,n):
    a = []
    for j in range(0,n):
        a.append(int(input("第%s行：" % (i + 1))))
    A.append(a)
else:
    for k in range(0,n):
        print A[k]
'''
for i in range(n):
    A.append([int(x) for x in raw_input("第%s行：" % (i + 1)).split()])
else:
    for i in range(n):
        for j in range(n):
            print ("%-3s" %A[i][j],end = ' ')
        else:
            print ("\n")

print ("please input matrix B:")
for i in range(0,n):
    b = []
    for j in range(0,n):
        b.append(int(input("第%s行：" % (i + 1))))
    B.append(b)
else:
    for k in range(0,n):
        print (B[k])

print ("matrixmul C = A * B:")
for i in range(0,n):
    c = []
    for j in range(0,n):
        sum = 0
        for k in range(0,n):
            sum = A[i][k] * B[k][j] + sum
        c.append(sum)
    C.append(c)
else:
    for k in range(0,n):
        print (C[k])
