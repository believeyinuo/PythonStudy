# -*- coding: utf-8 -*-
# @Time : 2019-08-26 14:00
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : unit_test_http_request.py
# @Project : PythonStudy

import unittest
from ddt import ddt, data
from PythonStudy.config_46.home_work.read_excel import ReadExcel
from PythonStudy.config_46.home_work.http_request import HttpRequest
from PythonStudy.config_46.home_work.reflection_get_data import GetData

test_data = ReadExcel("unit_test_excel.xlsx", "python").get_data()


@ddt
class UnitTestHttpRequest(unittest.TestCase):
    def setUp(self) -> None:
        print("我要开始执行测试用例了")

    def tearDown(self) -> None:
        print("测试用例执行完毕")

    @data(*test_data)
    def test_api(self, item):
        res = HttpRequest.http_request(item["url"], item["data"], item["method"], getattr(GetData, "Cookie"))
        if res.cookies:
            setattr(GetData, "Cookie", res.cookies)
        print("返回结果为{0}".format(res.json()))

        try:
            self.assertEqual(item["expected"], res.json("code"))
        except AssertionError as e:
            print("断言错误")
            raise e
