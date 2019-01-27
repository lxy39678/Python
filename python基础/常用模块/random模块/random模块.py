#!/usr/bin/python
# -*- coding:utf-8

import random

# 随机获取1到20之间的浮点数
print(random.uniform(1,20))

# 随机获取1到20之间的一个整数
print(random.randint(1,20))

# 随机获取seq的一个元素
print(random.choice(["tom""jin","jason"]))

# 随机获取seq中的K个元素
print(random.sample(["tom","jim","jason","jesse"],2))

# 打乱list里面的元素顺序
list_a = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(list_a)
print(list_a)