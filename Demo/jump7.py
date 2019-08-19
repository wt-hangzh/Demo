#!/usr/bin/env python
# or /usr/bin/python

for i in range(1,101):
    if i%7==0:
        continue
    if str(7) in str(i):
        continue
    print(i)

"""
for i in range(1,101):
    if i%7==0 or i%10==7 or i//10==7:
        continue
    print(i)
"""
