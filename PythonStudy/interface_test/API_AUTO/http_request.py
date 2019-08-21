# -*- coding:utf-8 -*-
# @Time : 2019-08-21
# @Author：lqc
# @Email:572948875@qq.com
# File : http_request.py

import requests


class HttpRequest:
    def http_request(self, url, data, method, cookies=None):
        if method.lower() == 'get':
            res = requests.get(url, data, cookies=cookies)
        else:
            res = requests.post(url, data, cookies=cookies)
        print("响应正文2：", res.json())
        return res#返回一个消息实体


if __name__ == '__main__':
    url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
    data = {"mobilephone": "18688773467", "pwd": "123456"}
    res = HttpRequest().http_request(url, data, 'post')

    recharge_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'
    recharge_data = {"mobilephone": "18688773467", "pwd": "123456"}
    HttpRequest().http_request(recharge_url, recharge_data, 'post', res.cookies)