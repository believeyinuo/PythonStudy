# -*- coding: utf-8 -*-
# @Time : 2019-08-26 14:13
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : unit_test_suite_http_request.py
# @Project : API_AUTO_test

import unittest
import HTMLTestRunner
from PythonStudy.config_46.home_work.unit_test_http_request import UnitTestHttpRequest

suite = unittest.TestSuite
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(UnitTestHttpRequest))

with open("test.html", "wb") as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title="python单元测试报告",
                                           description="lqc的第N次测试报告")
    runner.run(suite)