# -*- coding: utf-8 -*-
# @Time : 2019-08-22 14:08
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : http_request.py
# @Project : API_AUTO_test

import requests


class HttpRequest:

    def http_request(self, url, data, method, cookies=None):
        if method.lower() == 'get':
            res = requests.get(url, data, cookies=cookies, verify=False)
        else:
            res = requests.post(url, data, cookies=cookies, verify=False)
        return res
