#!/usr/bin/python
# -*- coding:utf-8

# 使用pytest实现对get_pinyin, get_initial, get_initials的单元测试
# 三个方法的行覆盖率要达到80%（这块老师课程没有覆盖到，鼓励学员自己查找pytest plugin插件获取到覆盖率的度量值）

from xpinyin import Pinyin
import pytest

class Test_pinyin:
    p = Pinyin()

    @pytest.mark.parametrize("chars,tone_marks,expect",[
        ("u你好","","u-ni-hao"),
        ("u你好","numbers","u-ni3-hao3"),
        ("u你好","marks","u-nǐ-hǎo"),
        ("nihao", "", "nihao"),
        ("ni好","","ni-hao"),
        ("你hao","","ni-hao")
    ])
    def test_get_pinyin(self,chars,tone_marks,expect):
        assert self.p.get_pinyin(chars=chars,tone_marks=tone_marks) == expect


    @pytest.mark.parametrize("char,expect",[
        ("你","N"),
        ("N","N"),
        ("n","n")
    ])
    def test_get_initial(self,char,expect):
        assert self.p.get_initial(char=char) == expect


    @pytest.mark.parametrize("chars,expect",[
        ("你好","N-H"),
        ("ni好","n-i-H"),
        ("你hao","N-h-a-o"),
        ("nihao","n-i-h-a-o")
    ])
    def test_get_initials(self,chars,expect):
        assert self.p.get_initials(chars=chars) == expect