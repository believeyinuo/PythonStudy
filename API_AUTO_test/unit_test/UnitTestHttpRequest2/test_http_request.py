# -*- coding: utf-8 -*-
# @Time : 2019-08-22 14:12
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : test_http_request.py
# @Project : API_AUTO_test


import unittest
from PythonStudy.unit_test.UnitTestHttpRequest2.http_request import HttpRequest
from PythonStudy.reflection.get_data import GetData


# COOKIE = None
# 第二条用例需要用到第一条用例的返回结果的某些值，怎么处理以来关系
# 1、全局变量  缺点：关联性比较强，一步错步步错
# 2、反射  缺点：关联性比较强，一步错步步错
# 3、setUp  缺点：关联性比较强，一步错步步错


class TestHttpRequest(unittest.TestCase):
    def setUp(self) -> None:
        print("我要开始执行测试用例了")

    def tearDown(self) -> None:
        print("测试用例执行完毕")

    def __init__(self, methodName, url, data, method, expected):  # 通过初始化参数传参
        super(TestHttpRequest, self).__init__(methodName)  # 保留父类的方法
        self.url = url
        self.data = data
        self.method = method
        self.expected = expected

    # 一个test代表一条用例，用for循环没用
    def test_api(self):
        res = HttpRequest().http_request(self.url, self.data, 'post', getattr(GetData, "Cookie"))
        if res.cookies:
            setattr(GetData, "Cookie", res.cookies)
        print("正常登录的返回{0}".format(res.json()))
        try:
            self.assertEqual(self.expected, res.json()["code"])
        except AssertionError as e:
            print("断言错误")
            raise e
