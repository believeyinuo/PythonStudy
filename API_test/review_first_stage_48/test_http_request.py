# -*- coding:utf-8 -*-
# @Time : 2019-08-26
# @Author：lqc
# @Email:572948875@qq.com
# File : test_http_request.py

import unittest
from PythonStudy.review_first_stage_48.http_request import HttpRequest


class TestHttpRequest(unittest.TestCase):
    def __init__(self, url, data, method, methodName):
        super(TestHttpRequest, self).__init__(methodName)
        self.url = url
        self.data = data
        self.method = method

    def setUp(self) -> None:
        print("我要开始测试了")

    def test_login(self):
        res = HttpRequest().http_request(self.url, self.data, self.method)
        print("测试请求的结果是:{0}".format(res.json()))

    def tearDown(self) -> None:
        print("我已经结束测试了")


class TestMath(unittest.TestCase):
    def test_add(self):
        print("a+b=", 10)

    def test_sub(self):
        print("a-b=", 20)
