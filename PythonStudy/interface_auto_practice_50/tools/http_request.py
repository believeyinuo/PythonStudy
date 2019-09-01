# -*- coding:utf-8 -*-
#@Time : 2019-08-27 
#@Author：lqc
#@Email:572948875@qq.com
#File : http_request.py

import requests
from PythonStudy.interface_auto_practice_50.tools.do_logging import MyLog


class HttpRequest:
    @staticmethod
    def http_request(url, data, http_method, cookie=None):
        try:
            if http_method.upper() == "GET":
                res = requests.get(url, data, cookies=cookie)
            elif http_method.upper() == "POST":
                res = requests.post(url, data, cookies=cookie)
            else:
                print("输入的请求方法不对")
                MyLog().info("输入的请求方法不对")
        except Exception as e:
            print("请求报错了:{0}".format(e))
            MyLog().error("请求报错了:{0}".format(e))
            raise e
        return res


if __name__ == "__main__":
    register_url = "http://47.107.168.87:8080/futureloan/mvc/api/member/register"
    register_data = {"mobilephone": "15096098888", "pwd": "123456", "regname":"小小"}

    login_url = "http://47.107.168.87:8080/futureloan/mvc/api/member/login"
    login_data = {"mobilephone": "15096098888", "pwd": "123456"}

    recharge_url = "http://47.107.168.87:8080/futureloan/mvc/api/member/recharge"
    recharge_data = {"mobilephone": "15096098888", "amount": "1000"}

    login_res = HttpRequest().http_request(login_url, login_data, "get")
    recharge_res = HttpRequest().http_request(recharge_url, recharge_data, "post", login_res.cookies)
    print("登录的结果：{}".format(login_res.json()))
    print("充值的结果：{}".format(recharge_res.json()))

# class HttpRequest:
#     def __init__(self, url, data, method, expected):
#         self.url = url
#         self.data = data
#         self.method = method
#         self.expected = expected
#
#     def http_request(self):
#         if self.method.lower() == "get":
#             res = requests.get(self.url, self.data)
#         else:
#             res = requests.post(self.url, self.data)
#         return res