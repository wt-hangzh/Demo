#!/usr/bin/env python2.7

import sys
def show():
    """
    ./copyfile.py file1 file2
    """
    return 1
print show.__doc__
print "sys.argv[1]:%s" % sys.argv[1]
print "sys.argv[2]:%s" % sys.argv[2]
print type(sys.argv)

f1 = sys.argv[1]
f2 = sys.argv[2]
s  = open(f1).read()
open(f1).close()
open(f2,"w").write(s)
open(f2).close()
