#!/usr/bin/python
# -*- coding:utf-8

import unittest

class simple_test(unittest.TestCase):
    def setUp(self):
        print("setup method")
        self.foo = list(range(10))
        print(str(self.foo))

    def test_1st(self):
        print('test_list')
        self.assertEqual(self.foo.pop(),9)

    def test_2nd(self):
        print('test_lnd')
        self.assertEqual(self.foo.pop(),9)

    def tearDown(self):
        print("end method")


if __name__=='__main__':
    unittest.main()