# -*- coding:utf-8 -*-
# @Time : 2019-08-21
# @Author：lqc
# @Email:572948875@qq.com
# File : unit_test.py

# 接口测试的本质 就是测试类里面的函数 通过数据驱动
# 单元测试的本质 测试函数 代码级别 通过代码级别

# 单元测试框架 unitest pytest+WEB->接口
# pytest+jenkins+allure

# 功能测试
# 1、写用例  TestCase
# 2、执行用例  1:TestSuite 存储用例 2:TestLoader 找用例，加载用例，存到1的TestSuite
# 3、对比实际结果  期望结果  判定用例是否通过  #断言Assert
# 4、出具测试报告 TextTestRunner

import unittest
from PythonStudy.unit_test.math_method import MathMethod


# 写一个测试类 对我们自己写的math_method模块里面的类进行单元测试
class TestMathMethod(unittest.TestCase):  # 继承了unittest里面的TestCase，专门用来写测试用例
    # 一个用例就是一个函数，不能传参，只有self关键字
    # 所有的用例（所有的函数都是test开头），不以test开头，无法识别它是一条用例

    #setUp执行每一条测试用例之前会执行setUp
    #tearDown 每一条测试用例执行完毕之后都会执行tearDown
    def setUp(self) -> None:#重写
        print("我要开始执行测试用例了")

    def tearDown(self) -> None:
        print("测试用例执行完毕")

    def test_add_two_positive(self):
        res = MathMethod(1, 1).add()
        print("1+1的结果值是", res)
        # 加一个断言，判断期望值与实际值的比对结果，一致就算通过，不一致，就算失败
        try:
            self.assertEqual(2, res)
        except AssertionError as e:
            print("断言错误是:{0}".format(e))
            raise e

    def test_add_two_zero(self):
        res = MathMethod(0, 0).add()
        print("0+0的结果值是", res)
        try:
            self.assertEqual(1, res, "两个0相加出错了")
        except AssertionError as e:
            print("断言错误是:{0}".format(e))
            raise e

    def test_add_two_negative(self):
        res = MathMethod(-1, -2).add()
        print("-1+-2的结果值是", res)
        self.assertEqual(-3, res)


class TestMulti(unittest.TestCase):  # 继承了unittest里面的TestCase，专门用来写测试用例
    # 一个用例就是一个函数，不能传参，只有self关键字
    # 所有的用例（所有的函数都是test开头），不以test开头，无法识别它是一条用例
    def test_multi_two_positive(self):
        res = MathMethod(1, 1).multi()
        print("1*1的结果值是", res)

    def test_multi_two_zero(self):
        res = MathMethod(0, 0).multi()
        print("0*0的结果值是", res)

    def test_multi_two_negative(self):
        res = MathMethod(-1, -2).multi()
        print("-1*-2的结果值是", res)

# if __name__ == "__main__":
#     unittest.main()

# ASCII编码
# test_add_two_positive
# test_add_two_zero
# test_add_two_negative
