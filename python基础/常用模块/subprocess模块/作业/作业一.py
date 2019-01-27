#!/usr/bin/python
# -*- coding:utf-8

import subprocess
import socket

# 1. 通过windows 下ping命令， 得出www.testerhome.com的服务器IP 地址
# a = subprocess.check_call("ping www.testerhome.com")
ip = socket.gethostbyname('www.testerhome.com')
print(ip)


# 2. 通过python启动一个windows应用程序
# 3. 在Linux下启动tomcat进程，并判断tomcat启动是否成功
note = subprocess.check_output("python",shell=True)
print(note)