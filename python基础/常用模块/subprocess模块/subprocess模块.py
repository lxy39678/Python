#!/usr/bin/python
# -*- coding:utf-8

# import commands(python3废弃)
import subprocess

# 获取命令执行后的输出结果
print(subprocess.getoutput("ls -al"))

# 返回一个元组，第一个元素是状态码，第二个元素是输出结果
print(subprocess.getstatusoutput("ls -al"))
print("*"*50)

# 执行windows下命令，返回执行执行状态结果
print(subprocess.call("ifconfig"))

# 执行windows下命令，返回执行执行状态结果
print(subprocess.check_call("ifconfig"))
print(subprocess.check_call("ifconfig",shell=True))

# 返回执行命令后的输出
print(subprocess.check_output("ifconfig"))
print(subprocess.check_output("ls",shell=True))