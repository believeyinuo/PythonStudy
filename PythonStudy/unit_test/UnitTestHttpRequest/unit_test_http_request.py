# 请完成http_request类的单元测试
# 要求如下：
# 1、针对http_request做作业
# 2、提供两个接口
# 3、针对登录接口写4个用例：正常登录、不输入密码、不输入账号、输入错误的密码
#    充值接口写4个用例：正常充值、不输入账号、不输入金额、输入错误的金额负数
# 4、请利用任何一种方法实现用例的加载并执行
# 5、生成Html类型的测试报告
# 注意：请在测试类里面加上异常处理以及断言

import unittest
import HTMLTestRunner

# 存储用例
suite = unittest.TestSuite()

# 创建一个加载器
loader = unittest.TestLoader()

from PythonStudy.unit_test.UnitTestHttpRequest import test_http_request

suite.addTest(loader.loadTestsFromModule(test_http_request))

# 执行
# with open("text.txt", "w+", encoding="utf-8") as file:
#     runner = unittest.TextTestRunner(stream=file, verbosity=1)
#     runner.run(suite)
with open("test_report.html", "wb") as file:
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           verbosity=2,
                                           title="python11期单元测试报告",
                                           description="python11期卡卡的第一次报告")
    runner.run(suite)

# excel处理 Excel处理测试数据、测试结果  pip install openpyxl
# 讲作业
# ddt pip install ddt

# pytest
