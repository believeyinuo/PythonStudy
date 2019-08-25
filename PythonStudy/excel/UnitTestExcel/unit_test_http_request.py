# -*- coding:utf-8 -*-
#@Time : 2019-08-24 
#@Author：lqc
#@Email:572948875@qq.com
#File : unit_test_http_request.py

import unittest
from PythonStudy.excel.UnitTestExcel.http_request import HttpRequest
from PythonStudy.excel.UnitTestExcel.reflection_get_data import GetData


class UnitTestHttpRequest(unittest.TestCase):
    def setUp(self) -> None:
        print("我要开始执行测试用例了")

    def tearDown(self) -> None:
        print("测试用例执行完毕")

    def __init__(self, methodName, url, data, method, expected):
        super(UnitTestHttpRequest, self).__init__(methodName)  # 保留父类的方法
        self.url = url
        self.data = data
        self.method = method
        self.expected = expected

    def test_api(self):
        res = HttpRequest.http_request(self.url, self.data, self.method, getattr(GetData, "Cookie"))
        if res.cookies:
            setattr(GetData, "Cookie", res.cookies)
        print("返回结果为{0}".format(res.json()))
        try:
            self.assertEqual(self.expected, res.json(["code"]))
        except AssertionError as e:
            print("断言错误")
            raise e