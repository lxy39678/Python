#!/usr/bin/python
# -*- coding:utf-8

import re

#将正则表达式编译成Pattern对象
pattern = re.compile(u'你好')
#使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match(u'你好，世界！')
print(match)
if match:
    #使用Match获取分组信息
    print("result:",match.group())
print("*"*50)


#将正则表达式编译成Pattern对象
pattern1 = re.compile(r'world')
# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
match = pattern1.search('hello world!')
if match:
    #使用Match获得分组信息
    print(match.group())
print("*"*50)

p = re.compile(r'\d+')
print(p.findall('one1two2three3four4'))