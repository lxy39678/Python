#!/usr/bin/env python
# encoding: utf-8


def demo_method(a, b, x):
    if a > 1 and b == 0:
        x = x/a
    if a == 2 or x > 1:
        x = x+1
    return x


if __name__=='__main__':
    print(demo_method(3, 0, 3))