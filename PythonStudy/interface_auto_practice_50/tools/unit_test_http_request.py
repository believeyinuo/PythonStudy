# -*- coding: utf-8 -*-
# @Time : 2019-08-28 10:42
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : unit_test_http_request.py
# @Project : PythonStudy

import unittest
from PythonStudy.interface_auto_practice_50.tools.http_request import HttpRequest
from PythonStudy.interface_auto_practice_50.tools.do_excel import DoExcel
from PythonStudy.interface_auto_practice_50.tools.get_cookie import GetCookie
from ddt import ddt, data  # 列表嵌套列表，列表嵌套字典
from PythonStudy.interface_auto_practice_50.tools.project_path import *

test_data = DoExcel(test_case_path, "login").do_excel()


@ddt
class TestHttpRequest(unittest.TestCase):
    # def __init__(self, url, data, method, cookies, methodName):
    #     super(TestHttpRequest, self).__init__(methodName)
    #     self.url = url
    #     self.data = data
    #     self.method = method
    #     self.cookies = cookies

    @data(*test_data)
    def test_http_request(self, item):
        res = HttpRequest().http_request(item["url"], eval(item["data"]), item["method"], getattr(GetCookie, "Cookie"))
        if res.cookies:
            setattr(GetCookie, "Cookie", res.cookies)
        try:
            self.assertEqual(str(item["expected"]), res.json()['code'])
            TestResult = 'PASS'
        except AssertionError as e:
            print("断言错误{0}".format(e))
            TestResult = 'Failed'
            raise e
        finally:
            DoExcel.write_back(test_case_path, item["sheet_name"], item["case_id"] + 1, res.text, TestResult)
        return res




