#!/usr/bin/env python
# encoding: utf-8

def py3exception():
    try:
        a = 1/0
    except Exception as e:
        print(e)

if __name__=='__main__':
    py3exception()