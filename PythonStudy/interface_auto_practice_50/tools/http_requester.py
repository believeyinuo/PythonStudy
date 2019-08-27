# -*- coding:utf-8 -*-
#@Time : 2019-08-27 
#@Author：lqc
#@Email:572948875@qq.com
#File : http_requester.py

import requests


class HttpRequest:
    def http_request(self, url, data, http_method, cookie=None):
        try:
            if http_method.upper() == "GET":
                res = requests.get(url, data, cookies=cookie)
            elif http_method.upper() == "POST":
                res = requests.post(url, data, cookies=cookie)
            else:
                print("输入的请求方法不对")
        except Exception as e:
            print("请求报错了:{0}".format(e))
            raise e
        return res


if __name__ == "__main__":
    register_url = "http://119.23.241.154:8080/fututeloan/mvc/api/member/register"
    register_data = {"mobilephone": "15096098888", "pwd": "123456"}

    login_url = "http://119.23.241.154:8080/fututeloan/mvc/api/member/login"
    login_data = {"mobilephone": "15096098888", "pwd": "123456"}

    recharge_url = "http://119.23.241.154:8080/fututeloan/mvc/api/member/login"
    recharge_data = {"mobilephone": "15096098888", "pwd": "123456"}

    login_res = HttpRequest().http_request(login_url, login_data, "get")
    recharge_res = HttpRequest().http_request(register_url, register_data, "post", login_res.cookies)
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