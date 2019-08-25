# -*- coding:utf-8 -*-
# @Time : 2019-08-24
# @Author：lqc
# @Email:572948875@qq.com
# File : http_request.py

import requests


class HttpRequest:
    def http_request(self, url, data, method, cookies=None):
        if method.lower() == 'get':
            res = requests.get(url, data, cookies=cookies, verify=None)
        else:
            res = requests.post(url, data, cookies=cookies, verify=None)
        return res
