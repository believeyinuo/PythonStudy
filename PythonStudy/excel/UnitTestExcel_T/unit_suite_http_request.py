# -*- coding:utf-8 -*-
#@Time : 2019-08-24 
#@Author：lqc
#@Email:572948875@qq.com
#File : unit_suite_http_request.py

import unittest
from PythonStudy.excel.UnitTestExcel.unit_test_http_request import UnitTestHttpRequest
from PythonStudy.excel.UnitTestExcel_T.do_excel import DoExcel

suite = unittest.TestSuite
for item in range(0, DoExcel().maxRow):
    suite.addTest(UnitTestHttpRequest("test_api",
                                      DoExcel().readExcel(item, 0),
                                      DoExcel().readExcel(item, 1),
                                      DoExcel().readExcel(item, 2),
                                      DoExcel().readExcel(item, 3)))