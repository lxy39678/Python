#!/usr/bin/python
# -*- coding:utf-8

import pytest

@pytest.mark.parametrize("x,y",[
      (3+5,8),
      (2+4,6),
      (6*9,54),
      ("testerhome","testerhome")

])

def test_add(x,y):
    assert x==y
