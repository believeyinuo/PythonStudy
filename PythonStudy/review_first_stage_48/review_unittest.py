# -*- coding:utf-8 -*-
#@Time : 2019-08-26 
#@Author：lqc
#@Email:572948875@qq.com
#File : review_unittest.py
#                                Result
#                                TestResult
#
# Loader                                            runner
# TestLoader                            TextTestResult  TextTestRunner
# MethodPrefix="test"                                   run(test)
# addTestsFromTestCase(testCaseClass)
#
#                                     suite
#                                   TestSuite
#                                   self._tests = []
#                                   run(result)
#
#
#                                     case
#                                    TestCase
#                                    setUp()
#                                    tearDown()
#                                    run(result)

# unittest核心步骤
# unittest中最核心的四个概念是：test case, test suite, test runner, test fixture
# TestCase:一个TestCase的实例就是一个测试用例
# TestSuite:多个测试用例集合在一起
# TestLoader:用来加载TestCase到TestSuite中的
# TestTestRunner:用来执行测试用例的。其中的run(test)会执行TestSuite/TestCase中的run(result)方法
# TestTestResult:保存TextTestRunner执行的测试结果
# fixture:测试用例环境的搭建和销毁。测试前准备环境的搭建(setUp)，执行测试代码(run)以及测试后环境的还原(tearDown)

# TestCase的使用
# 继承unittest里面的TestCase类，继承这个类，写测试用例
# 每个用例都要记得引入fixture，做一些准备以及结束的工作
# 编写测试用例步骤：
# 1、引入unittest模块、被测文件或者其中的类
# 2、创建一个测试类，并继承unittest.TestCase
# 3、重写setUp和tearDown方法（如果有初始化条件和结束条件）
# 4、定义测试函数，函数名以test_开头
# 5、调用unittest.main()方法运行测试用例

# 测试用例参数化
# 参数化来传递数据
# 超继承
# ddt
# excel
# 反射、全局变量cookie的传递

# TestSuite&TestLoader的使用
# TestSuite：测试集，把所有的用例都存进来。常用的方法如下
# unittest.TestSuite()
# 方法一：addTest() 添加一个测试用例
# 方法二：addTests([...]) 添加多个测试用例 添加用例的方式是一样的
#
# unittest.TestLoader()
# 方法一：unittest.TestLoader.loadTestsFromModule(模块名)#不需要加引号
# 方法二：unittest.TestLoader.loadTestsFromTestCase(测试类名)#不需要加引号

# 完整的单元测试很少只执行一个测试用例，开发人员通常需要编写多个测试用例才能对某一软件功能进行比较完善的测试，这些相关的测试用例称为一个测试用例集，用TestSuite类来表示的，用到的是TestSuite(),用addTest

