#!/usr/bin/python
# -*- coding:utf-8

# 1. 在不同模块中输出log信息到同一个文件test.log上，要求log输出不同级别的log， 包括输出异常信息到log文件
import logging
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
from 常用模块.log模块.morelog import testlog

def logNot():

    logging.basicConfig(filename="test.log",level=0,
    format='%(asctime)s %(name)s %(levelname)s %(module)s:%(lineno)d %(message)s')

    logging.debug("this is debug log")
    logging.info("this is info log")
    logging.exception("this is info_log")
    testlog()

logNot()