#!/usr/bin/python
# -*- coding:utf-8

import configparser

def get_cfg(in_file):
    config = configparser.ConfigParser()
    config.read(in_file)
    return config

cfg = get_cfg("test.cfg")

# 获取配置文件中所有的sections
print(cfg.sections())

# 获取指定section下对应option的值
print(cfg.get("mail_server","smtp_host"))

# 判断配置文件中是否有对应session
print(cfg.has_section("test"))

# 判断对应section是否有对应的option
print(cfg.has_option("mail_server","test"))