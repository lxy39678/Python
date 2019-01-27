#!/usr/bin/python
# -*- coding:utf-8

#在Linux下每隔1分钟检查一下sleep进程是不是在运行，如果sleep进程退出了，立即启动sleep进程

# import paramiko
#
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('',username='01978968@shell.testing-studio.com',password='testerhome')

import psutil
from time import sleep
import os

pids = psutil.pids()


a = 0
for pid in pids:
    p = psutil.Process(pid)
    # print(pid,p.name())

    if(p.name() == 'sleep'):
        a += 1
        print(a)


if(a == 0):
    os.system("sleep 5 &")
    print('****')


