# -*- coding:utf-8 -*-
#@Time : 2019-08-24 
#@Author：lqc
#@Email:572948875@qq.com
#File : unit_test_http_request.py

import unittest
from PythonStudy.ddt_44.do_excel import DoExcel
from PythonStudy.excel.UnitTestExcel.reflection_get_data import GetData
from ddt import ddt,data
from PythonStudy.ddt_44.http_request import HttpRequest

test_data = DoExcel("unit_test_excel.xlsx", "python").get_data()


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
            self.assertEqual(item["expected"], res.json(["code"]))
        except AssertionError as e:
            print("断言错误")
            raise e