#!/usr/bin/python
# -*- coding:utf-8

import random


def add(x,y):
    return x+y

def test_add():
    random_value = random.randint(2,6)
    print("random_value:"+str(random_value))
    assert add(1,3) == random_value