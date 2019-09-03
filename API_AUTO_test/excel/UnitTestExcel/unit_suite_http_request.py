# -*- coding:utf-8 -*-
#@Time : 2019-08-24 
#@Author：lqc
#@Email:572948875@qq.com
#File : unit_suite_http_request.py

import unittest
from PythonStudy.excel.UnitTestExcel.unit_test_http_request import UnitTestHttpRequest
from PythonStudy.excel.UnitTestExcel.read_excel import ReadExcel

suite = unittest.TestSuite
for item in range(0, ReadExcel().maxRow):
    suite.addTest(UnitTestHttpRequest("test_api",
                                      ReadExcel().readExcel(item, 0),
                                      ReadExcel().readExcel(item, 1),
                                      ReadExcel().readExcel(item, 2),
                                      ReadExcel().readExcel(item, 3)))