#!/usr/bin/env python2.7

from __future__ import print_function

cpu = open("/proc/cpuinfo")
while True:
    s = cpu.readline()
    if "cpu MHz" in s:
        print (s)
        break
