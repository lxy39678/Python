#!/usr/bin/python
# -*- coding:utf-8

#搜索find/下所有以test开头，py结尾的文件（包括子目录的），把文件全路径输出到一个列表里面打印出来

import os

for dirpath,dirs,files in os.walk("./find"):
    for name in files:
        if(os.path.splitext(name)[1] == '.py'):
            if(os.path.splitext(name)[0] == 'test'):
                filepath = os.getcwd() + dirpath[1:] + '/' + name
                print(filepath)

