# -*- coding:utf-8 -*-
# @Time : 2019-09-14 19:03
# @Author：lqc
# @Email:572948875@qq.com
# File : test_login.py

import unittest
from selenium import webdriver
from WEB_AUTO_test.pageobject_95.PageObjects.login_page import LoginPage
from WEB_AUTO_test.pageobject_95.PageObjects.index_page import IndexPage
from WEB_AUTO_test.pageobject_95.TestDatas import Common_Datas as CD
from WEB_AUTO_test.pageobject_95.TestDatas import login_datas as LD
import ddt


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 通过excel读取本功能当中需要的所有测试数据
        print("========所有测试用例之前的，setup============整个测试类只执行一次========")
        cls.driver = webdriver.Chrome()
        cls.driver.get(CD.web_login_url)
        cls.lg = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        print("========所有测试用例之后的，tearDown============整个测试类只执行一次========")
        cls.driver.quit()

    # def setUp(self) -> None:
    #     # 前置：访问登录页面
    #     pass

    def tearDown(self) -> None:
        # 后置
        self.driver.refresh()

    # 正常用例-登录成功
    def test_login_1_success(self):
        # 步骤  输入用户名：XXX  密码：XXX 点击登录
        self.lg.login(LD.success_data["user"], LD.success_data["password"])
        # 断言  首页当中-能否找到 退出 这个元素
        self.assertTrue(IndexPage(self.driver).isExist_Logout_ele())

    # 异常用例-手机号码格式不正确(大于11位、小于11位、为空、不在号码段) ddt
    @ddt.data(*LD.phone_data)
    def test_login_0_user_wrongFormat(self, data):
        # 步骤  输入用户名：XXX  密码：XXX 点击登录
        self.lg.login(data["user"], data["password"])
        # 断言  登录页面 提示：请输入正确的手机号码
        # 登录页面中  -  获取提示框的文本内容
        # 比对文本内容 与  期望的值 是否相等
        self.assertEqual(self.lg.get_errorMsg_from_loginArea(), data["check"])

    def test_login_0_wrongPwd_noReg(self):
        # 步骤  输入用户名：XXX  密码：XXX 点击登录
        # 断言  登录页面 页面正中间提示：XXX
        # 登录页面中  -  获取提示框的文本内容
        # 比对文本内容 与  期望的值 是否相等
        pass

    # 异常用例-用户名为空
    def test_login_0_noUser(self):
        # 步骤  输入用户名：XXX  密码：XXX 点击登录
        self.lg.login("", "python")
        # 断言  登录页面 提示：请输入手机号
        pass

    # 异常用例-未注册手机号
    # 异常用例-错误的密码
    # 异常用例-不输入密码
