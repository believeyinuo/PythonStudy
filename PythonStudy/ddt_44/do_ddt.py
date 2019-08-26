# -*- coding: utf-8 -*-
# @Time : 2019-08-26 09:59
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : do_ddt.py
# @Project : PythonStudy

# ddt ddt+unittest 来进行数据的处理 第三方库
# 装饰器 会在你的函数运行之前运行
from ddt import ddt, data, unpack
import unittest

# test_data = [[1, 3], [4, 5, 8]]
test_data = [{"no": 1, "name":"文档"},
             {"no": 2, "name":"小黄"}]

@ddt  # 装饰测试类
class RestMath(unittest.TestCase):

    @data(*test_data)  # 装饰测试方法，拿到几个数据，就执行几条用例
    @unpack  # 根据逗号进行分割  如果unpack后的参数 少于5个 推荐用unpack 要注意参数不对等的情况 提供对应的个数的参数来接受

    # 如果要对字典进行unpack，参数名与字典key对应
    def test_print_data(self, no, name):
        print("no:", no)
        print("name:", name)
        # print("c:", c)

    # def test_add(self):
    #     a = 10
    #     b = 20
    #     print(a + b)

#unnittest单元测试  通过单元测试 实现对自己写的类的测试
#TestCase self.assert 异常处理

#参数化
#写成类
#超继承->原理要懂  DDT->推荐DDT


