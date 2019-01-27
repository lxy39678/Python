#!/usr/bin/env python
# encoding: utf-8

def py2excption():
    try:
        a = 1/0
    except Exception,e:
        print e


if __name__=='__main__':
    py2excption()