#!/usr/bin/python
# -*- coding:utf-8
import time
from datetime import datetime
from datetime import timedelta

# 获取1970.1.1.0:0:0 到当前的时间
print(time.time())

#获取本地时间
print(time.localtime())

#获取格里尼治时间
print(time.gmtime())

#格式化时间格式
print(time.strftime("%y/%m/%d %H:%M"))
print(time.strftime("%Y-%m-%d %H:%M:%S %Z"))
print(time.strftime("%c"))
print("*"*50)
#字符串时间格式转化为时间
time_tuple = time.strptime("1 Jan 2018 1:30pm","%d %b %Y %I:%M%p")
print(type(time_tuple))

# • time.mktime(): 将时间元组转换为1970/1/1 0:0:0 到目前的时间值
#计算两个datetime对象的时间差
d1 = datetime.strptime('2017-12-05 17:41:20','%Y-%m-%d %H:%M:%S')
d2 = datetime.strptime('2017-12-03 19:40:28','%Y-%m-%d %H:%M:%S')
delta = d2 - d1
print(delta)

print(datetime.now())
print(datetime.utcnow())
print(datetime.now().strftime("%y/%m/%d %H:%M"))
date_format = datetime.now().strptime("1 Jan 2018 1:30pm", "%d %b %Y %I:%M%p")

#后三天
now = datetime.now()
days_delta = timedelta(days=3)
print(now+days_delta)

hours_delta = timedelta(hours=0.5)
print(now+hours_delta)

mins_delta = timedelta(minutes=10)
print(now+mins_delta)