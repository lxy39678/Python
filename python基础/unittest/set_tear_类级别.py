#!/usr/bin/python
# -*- coding:utf-8

import unittest

class simple_test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print("setup method")
        self.foo = list(range(10))
        print(str(self.foo))

    def test_1st(self):
        print('test_list')
        self.assertEqual(self.foo.pop(),9)

    def test_2nd(self):
        print('test_2nd')
        self.assertEqual(self.foo.pop(),8)

    @classmethod
    def tearDownClass(self):
        print("end_method")


if __name__=='__main__':
    unittest.main()