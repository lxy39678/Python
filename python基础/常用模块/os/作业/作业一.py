#!/usr/bin/python
# -*- coding:utf-8

#在当前目录创建test/log.txt，如果文件最后修改时间是在1小时之前，把文件打包压缩，备份到/test1/log.txt目录下

import os
import time
from time import sleep
from zipDir import zipDir

os.mkdir("test")
f = open("./test/log.txt","w")

#获取修改时间
mtime = os.path.getmtime("./test/log.txt")

now = time.time()

if(now-mtime)<86400:
    os.mkdir("test1")
    zipDir("./test","./test1/log.zip")



