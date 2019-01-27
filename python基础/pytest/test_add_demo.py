#!/usr/bin/python
# -*- coding:utf-8
import time
import random

def add(x,y):
    return x+y


def test_add():
    time.sleep(random.randint(1,5))
    assert add(1,2) == 3

def test_add2():
    time.sleep(random.randint(1, 3))
    assert add(3,2) == 3

def test_add3():
    time.sleep(random.randint(2, 6))
    assert add('tester','home') == 'testerhome'
