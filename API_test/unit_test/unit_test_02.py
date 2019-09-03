# -*- coding:utf-8 -*-
#@Time : 2019-08-21 
#@Author：lqc
#@Email:572948875@qq.com
#File : unit_test_02.py

import unittest
# import HTMLTestRunnerNew#写好的一个模块，可以直接使用
from PythonStudy.unit_test.unit_test import TestMathMethod

#A class whose instances are single test cases
#这个类的实例是一个单独的用例

suite = unittest.TestSuite()#存储用例
#方法一：
#只执行一条 两个正数相加
# suite.addTest(TestMathMethod("test_add_two_positive"))

#方法二：TestLoadder
loadder = unittest.TestLoader()#创建一个加载器
# suite.addTest(loadder.loadTestsFromTestCase(TestMathMethod))
from PythonStudy.unit_test import unit_test
suite.addTest(loadder.loadTestsFromModule(unit_test))

#执行 上下文管理器-原始的
with open("text.txt", "w+", encoding="utf-8") as file:
    runner = unittest.TextTestRunner(stream=file, verbosity=0)
    runner.run(suite)
print(file.closed)

#新鲜 html
# with open("test_report.html", "wb") as file:
#     runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, verbosity = 2,title = "python11期单元测试报告",descripthon = "python11期卡卡的第一次报告", tester = "卡卡")
#     runner.run(suite)
