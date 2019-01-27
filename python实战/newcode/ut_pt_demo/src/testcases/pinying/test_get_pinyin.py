#!/usr/bin/env python
# encoding: utf-8

from xpinyin import Pinyin

class TestDefaultValue:

    def test_all_default(self):

        assert Pinyin().get_pinyin() == 'ni-hao'
