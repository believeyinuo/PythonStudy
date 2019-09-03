# -*- coding:utf-8 -*-
#@Time : 2019-08-26 
#@Author：lqc
#@Email:572948875@qq.com
#File : review_inherit_father.py

import requests


class HttpRequest:
    def __init__(self, url, data):
        self.url = url
        self.data = data
        print("此处代表一万行代码")

    def get_request(self):
        res = requests.get(self.url, self.data)
        print("get请求的结果是{0}".format(res))

    def post_request(self):
        res = requests.post(self.url, self.data)
        print("post请求的结果是{0}".format(res))