#!/usr/bin/env python2.7

print("True or False:")

for elenment in ['', 'S', [], [1, 2], {}, {3, 'SSS'}, 0, 0.0, 1, None]:
    if elenment:
        print(elenment, True) 
    else:
        print(elenment, False) 
