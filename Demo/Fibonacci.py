#!/usr/bin/env python2.7

from __future__ import print_function

a, b = 0, 1
while b < 100:
    print(b,end=' ')
    a, b = b, a + b
print()
