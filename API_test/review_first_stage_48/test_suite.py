# -*- coding:utf-8 -*-
# @Time : 2019-08-26
# @Author：lqc
# @Email:572948875@qq.com
# File : test_suite.py

import unittest
from PythonStudy.review_first_stage_48.test_http_request import TestHttpRequest

# 收集用例TestSuite
suite = unittest.TestSuite()

# 加载用例
# 方法一：测试类里面的一个实例 就是一个测试用例
# url = 'https://client.xsdsport.com/erasports/client/customer/login'
# data_normal = {"mobilephone": "13068712118", "pwd": "123456"}
# data_err_pwd = {"mobilephone": "13068712118", "pwd": "12345678"}
# suite.addTest(TestHttpRequest(url, data_normal, "get", "test_login"))
# suite.addTest(TestHttpRequest(url, data_err_pwd, "get", "test_login"))
test_data = [{"url":"https://client.xsdsport.com/erasports/client/customer/login",
              "data":{"mobilephone": "13068712118", "pwd": "123456"}, "method":"get",
              "title":"正常测试"},
             {"url":"https://client.xsdsport.com/erasports/client/customer/login",
              "data":{"mobilephone": "13068712118", "pwd": "1234567"}, "method":"get",
              "title":"密码错误测试"}]
for item in test_data:
    suite.addTest(TestHttpRequest(item["url"], item["data"], item["method"], "test_login"))

# 方法二：TestLoader
# loader = unittest.TestLoader()  # 用例加载器
# suite.addTest(loader.loadTestsFromTestCase(TestHttpRequest))
# loadTestsFromTestCase 一次性加载某个测试类里面的所有测试用例

# loadTestsFromModule   一次性加载某个模块下面的所有用例  某个模块下面有多个测试类
# from API_test.review_first_stage_48 import test_http_request
#
# suite.addTest(loader.loadTestsFromModule(test_http_request))

# 执行用例
runner = unittest.TextTestRunner()
runner.run(suite)
