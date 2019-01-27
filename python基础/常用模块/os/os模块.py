#!/usr/bin/python
# -*- coding:utf-8

import os

# 返回指定目录下的所有文件和目录名，不包括子目录
print(os.listdir("."))

# 返回当前Python进程正在工作的目录
print(os.getcwd())

# 获得文件属性，文件大小，创建时间，最后访问时间等
print(os.stat("filexample.txt"))

# 运行shell命令
print(os.system("ls"))

# 连接目录与文件名或目录
print(os.path.join("常用模块/","文件读写.py"))

# 创建目录
os.mkdir("name")
print(os.listdir("."))

# 删除多个目录
os.removedirs("name")
print(os.listdir("."))

# 返回文件名
print(os.path.basename("/Users/lixiangyu/PycharmProjects/python基础/常用模块/__init__.py"))
