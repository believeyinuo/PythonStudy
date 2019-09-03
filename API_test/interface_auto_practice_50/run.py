# -*- coding:utf-8 -*-
# @Time : 2019-08-27
# @Author：lqc
# @Email:572948875@qq.com
# File : run.py
# 执行文件

from PythonStudy.interface_auto_practice_50.tools.unit_test_http_request import TestHttpRequest
# from API_test.interface_auto_practice_50.tools.do_excel import DoExcel
# from API_test.interface_auto_practice_50.tools.get_data import GetData
from PythonStudy.interface_auto_practice_50.tools.project_path import *
import unittest
import HTMLTestRunner
# from API_test.interface_auto_practice_50.tools import unit_test_http_request

suite = unittest.TestSuite()

# test_data = DoExcel(test_case_path, "login").do_excel()

# for item in test_data:
#     res = TestHttpRequest(item["url"], item["data"], item["method"]), getattr(GetCookie, "Cookie"), "test_http_request")
#     if res.cookies:
#         setattr(GetCookie, "Cookie", res.cookies)
#     suite.addTest(res)

loader = unittest.TestLoader()
# suite.addTest(TestHttpRequest('test_api'))
# suite.addTest(loader.loadTestsFromModule(unit_test_http_request))
suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))

with open(test_report_path, 'wb') as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           title='这个是单元测试报告',
                                           description='这个是单元测试报告')
    runner.run(suite)

# from API_test.interface_auto_practice_50.tools.http_request import HttpRequest
# from API_test.interface_auto_practice_50.tools.do_excel import DoExcel
# from API_test.interface_auto_practice_50.tools.get_cookie import GetCookie
#
# COOKIE = None
#
# # test_data = [{"url": "http://119.23.241.154:8080/futureloan/mvc/api/member/login",
# #               "data": {"mobilephone": "15096098888", "pwd": "123456"},
# #               "description": "正常登录", "http_method": "get"},
# #              {"url": "http://119.23.241.154:8080/futureloan/mvc/api/member/login",
# #               "data": {"mobilephone": "15096098888", "pwd": "123456789"},
# #               "description": "输入错误的密码登录", "http_method": "get"}]

# test_data = DoExcel("/Users/szdl/Desktop/API_test/API_test/interface_auto_practice_50/test_data/interface_auto_practice.xlsx", "login").do_excel()
#
#
# def run():
#     # global COOKIE
#     for item in test_data:
#         print("正在测试的用例是{0}".format(item["description"]))
#         # res = HttpRequest().http_request(item["url"], item["data"], item["http_method"], COOKIE)
#         res = HttpRequest().http_request(item["url"], item["data"], item["method"], getattr(GetCookie, 'Cookie'))
#         if res.cookies:
#             setattr(GetCookie, 'Cookie', res.cookies)
#         #     COOKIE = res.cookies
#         print("充值的结果：{}".format(res.json()))
#         DoExcel().write_back(item["case_id"] + 1, str(res.json()))
#
#
# run()
