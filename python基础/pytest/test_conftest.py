#!/usr/bin/python
# -*- coding:utf-8

import pytest

@pytest.fixture(scope='session',autouse=True)
def build_db_connection():
    print('building database connection')
    yield
    print('close database connection')