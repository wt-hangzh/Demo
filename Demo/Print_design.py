#!/usr/bin/env python2.7

print "-"*31

i = 1
j = 20
n = 31
while i <= 20:
    print " "*((n-i)/2)+"*"*i+" "*((n-i)/2)
    i += 2


while j >= 1:
    print " "*((n-j)/2)+"*"*j," "*((n-j)/2)
    j -= 2

print "-"*31

