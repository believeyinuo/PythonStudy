# -*- coding: utf-8 -*-
# @Time : 2019-08-22 14:12
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : test_http_request.py
# @Project : API_AUTO_test


import unittest
from PythonStudy.unit_test.UnitTestHttpRequest.http_request import HttpRequest
from PythonStudy.reflection.get_data import GetData

# COOKIE = None
# 第二条用例需要用到第一条用例的返回结果的某些值，怎么处理以来关系
# 1、全局变量  缺点：关联性比较强，一步错步步错
# 2、反射  缺点：关联性比较强，一步错步步错
# 3、setUp  缺点：关联性比较强，一步错步步错


test_data = [{"data": {"mobilephone": "18688773467", "pwd": "123456"}, "expected": "1000"},
             {"data": {"mobilephone": "18688773467", "pwd": ""}, "expected": "999"},
             {"data": {"mobilephone": "", "pwd": "123456"}, "expected": "999"},
             {"data": {"mobilephone": "18688773467", "pwd": "12345678"}, "expected": "120"}];


class TestHttpRequest(unittest.TestCase):
    def setUp(self) -> None:
        self.login_url = "http://192.168.31.196:8007/erasports/client/customer/login"
        self.recharge_url = "http://192.168.31.196:8007/erasports/client/customer/recharge"
        # self.normal_login_data = {"action": "301",
        #                           "client_id": "",
        #                           "language": "zh",
        #                           "pwd": "e10adc3949ba59abbe56e057f20f883e",
        #                           "reqtimestamp": "1566454740",
        #                           "sign": "4ee321d1c702b574c9900c195032d647",
        #                           "terminal_no": "ios",
        #                           "token": "",
        #                           "user": "13068712118",
        #                           "version": "2.0.12",
        #                           "ztid": "15664547401864"}
        self.normal_login_res = HttpRequest().http_request(self.login_url, self.normal_login_data, 'post')
        # self.cookies = self.normal_login_res.cookies
        print("我要开始执行测试用例了")

    def tearDown(self) -> None:
        print("测试用例执行完毕")

    # 一个test代表一条用例，用for循环没用
    def test_normal_login(self):
        # global COOKIE  # 声明全局变量
        if self.normal_login_res.cookies:
            #     COOKIE = self.normal_login_res.cookies
            setattr(GetData, "Cookie", self.normal_login_res.cookies)
        print("正常登录的返回{0}".format(self.normal_login_res.json()))

    def test_no_name_login(self):
        no_name_login_data = {"action": "301",
                              "client_id": "",
                              "language": "zh",
                              "pwd": "e10adc3949ba59abbe56e057f20f883e",
                              "reqtimestamp": "1566454740",
                              "sign": "4ee321d1c702b574c9900c195032d647",
                              "terminal_no": "ios",
                              "token": "",
                              "user": "",
                              "version": "2.0.12",
                              "ztid": "15664547401864"}
        no_name_login_res = HttpRequest().http_request(self.login_url, no_name_login_data, 'post')
        print("无用户名登录的返回{0}".format(no_name_login_res.json()))
        try:
            self.assertEqual('999', no_name_login_res.json()["code"])
        except AssertionError as e:
            print("断言错误：登录失败,原因是{0}".format(no_name_login_res.json()["note"]))
            raise e  # 抛出异常

    def test_no_pwd_login(self):
        no_pwd_login_data = {"action": "301",
                             "client_id": "",
                             "language": "zh",
                             "pwd": "",
                             "reqtimestamp": "1566454740",
                             "sign": "4ee321d1c702b574c9900c195032d647",
                             "terminal_no": "ios",
                             "token": "",
                             "user": "13068712118",
                             "version": "2.0.12",
                             "ztid": "15664547401864"}
        no_pwd_login_res = HttpRequest().http_request(self.login_url, no_pwd_login_data, 'post')
        print("无密码登录的返回{0}".format(no_pwd_login_res.json()))
        try:
            self.assertEqual('999', no_pwd_login_res.json()["code"])
        except AssertionError as e:
            print("断言错误：登录失败,原因是{0}".format(no_pwd_login_res.json()["note"]))
            raise e

    def test_wrong_pwd_login(self):
        wrong_pwd_login_data = {"action": "301",
                                "client_id": "",
                                "language": "zh",
                                "pwd": "123456",
                                "reqtimestamp": "1566454740",
                                "sign": "4ee321d1c702b574c9900c195032d647",
                                "terminal_no": "ios",
                                "token": "",
                                "user": "13068712118",
                                "version": "2.0.12",
                                "ztid": "15664547401864"}
        wrong_pwd_login_res = HttpRequest().http_request(self.login_url, wrong_pwd_login_data, 'post')
        print("密码错误登录的返回{0}".format(wrong_pwd_login_res.json()))
        try:
            self.assertEqual('120', wrong_pwd_login_res.json()["code"])
        except AssertionError as e:
            print("断言错误：登录失败,原因是{0}".format(wrong_pwd_login_res.json()["note"]))
            raise e
