#!/usr/bin/python
# -*- coding:utf-8

import unittest.HTMLTestRunner
import unittest
import unittest.unitdemo

report_title = '执行报告'
desc = '测试用例执行报告'
report_file = 'ExampleReport.html'
testsuite = unittest.TestSuite()
testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(unitdemo.TAdd))

with open(report_file,'wb') as report:
    runner = htmltestrunner.HTMLTestRunner(stream=report,title=report_title,description=desc)
    runner.run(testsuite)

