#!/usr/bin/env python2.7
#coding=utf-8

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

if __name__ == '__main__':
   app.run(host="192.168.0.112",port=8060)
