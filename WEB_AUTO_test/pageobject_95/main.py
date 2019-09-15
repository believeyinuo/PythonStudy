# -*- coding:utf-8 -*-
# @Time : 2019-09-15 18:50
# @Author：lqc
# @Email:572948875@qq.com
# File : main.py

import unittest
import HTMLTestRunner
from WEB_AUTO_test.pageobject_95.Common.dir_config import *

# 实例化套件对象
s = unittest.TestSuite()

# TestLoader的用法
# 1、实例化TestLoader对象
# 2、使用discover去找到一个目录下的所有测试用例
# 3、使用s
loader = unittest.TestLoader()
s.addTests(loader.discover(testcases_dir))

# # 运行
# runner = unittest.TextTestRunner()
# runner.run(s)

fp = open(htmlreport_dir + '/autoTest_report.html', 'wb')
runner = HTMLTestRunner(
    stream = fp,
    title = "单元测试报告",
    description = "单元测试报告",
    tester = "小简"
)
runner.run(s)