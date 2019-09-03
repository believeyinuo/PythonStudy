# -*- coding: utf-8 -*-
# @Time : 2019-08-26 14:42
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : review_function.py
# @Project : API_test

import requests


class HttpRequest:

    a = 6666666666
    # 完成http请求
    # def __init__(self, url, data):
    #     self.url = url
    #     self.data = data

    # 实例方法，只能通过实例来调用
    # @staticmethod
    def get_request(self, url, data):
        res = requests.get(url, data)
        print("返回的结果是{0}".format(res))

    def post_request(self, url, data):
        res = requests.post(url, data)
        print("返回的结果是{0}".format(res))

    @classmethod
    def add(cls):
        print("我是类方法")
        return 10

    @staticmethod
    def print_msg():
        print("Python的同学又皮又痒")

# 类方法  静态方法  -->>  可以直接类名.方法名调用
#                -->>  可以实例调用
# 用不到初始化函数里面类的属性值
HttpRequest.add()
HttpRequest.print_msg()

# 实例方法 -->> 必须要创建实例来调用
# 初始化函数里面类的属性值只能实例方法调用
url = 'https://client.xsdsport.com/erasports/client/customer/login'
data = {"mobilephone":"13068712118", "pwd": "123456"}
# HttpRequest.get_request(url,data)
# TypeError: get_request() missing 1 required positional argument: 'data'
HttpRequest().get_request(url,data)
print(HttpRequest.a)

