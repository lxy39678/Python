#!/usr/bin/python
# -*- coding:utf-8

import json

python_dic = {'name':'fengcheng',u'sex':"Male",'c':3,'d':4,'e':5}
print(type(json.dumps(python_dic,ensure_ascii="utf-8")))
print(json.dumps(python_dic,ensure_ascii="utf-8"))

json_str = '{"name":"fengcheng","sex":"Male","c":3,"d":4,"e":5}'
print(type(json.loads(json_str,encoding="utf-8")))
print(json.loads(json_str,encoding="utf-8"))