#!/usr/bin/python
# -*- coding:utf-8

import pytest

def add(x,y):
    return x+y

def test_add3():
    pytest.assume(add(4,2)==3)
    pytest.assume(add(1,2)==3)
    pytest.assume(add(2,2)==8)
