#!/usr/bin/env python2.7

print("compute powerseries: e^x = 1 + x + x^2 / 2! + x^3 / 3! + ... + x^n / n! (0 < x < 1)")

x = float(input("Enter the value of x: "))
n = term = num = 1
result = 1.0
while n <= 100:
    term *= x / n
    result += term
    n += 1
    if term < 0.0001:
        break
print("No of Times= {} and Sum= {}".format(n, result))

import math
print "if x == 0.5,the answer == sqrt(e) :",math.sqrt(math.e)
print "if x == 1  ,the answer ==     (e) :",math.e


