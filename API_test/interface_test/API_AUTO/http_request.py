# -*- coding:utf-8 -*-
# @Time : 2019-08-21
# @Author：lqc
# @Email:572948875@qq.com
# File : http_request.py

import requests


class HttpRequest:
    def http_request(self, url, data, method, cookies=None):
        if method.lower() == 'get':
            res = requests.get(url, data, cookies=cookies, verify = False)
        else:
            res = requests.post(url, data, cookies=cookies, verify = False)
        print("响应正文2：", res.json())
        return res#返回一个消息实体


if __name__ == '__main__':
    # url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/login'
    # data = {"mobilephone": "18688773467", "pwd": "123456"}
    # res = HttpRequest().http_request(url, data, 'post')
    #
    # recharge_url = 'http://119.23.241.154:8080/futureloan/mvc/api/member/recharge'
    # recharge_data = {"mobilephone": "18688773467", "pwd": "123456"}
    # HttpRequest().http_request(recharge_url, recharge_data, 'post', res.cookies)

    login_url = "https://www.ketangpai.com/UserApi/login"
    data = {"email":"1255811581@qq.com","password": "huahua90!@", "remeber": 0}
    res = HttpRequest().http_request(login_url, data, 'post')
    print("课堂派登录的结果是：{0}".format(res))
    print("课堂派登录的结果coookies是：{0}".format(res.cookies))


    kq_url = 'https://www.ketangpai.com/SummaryApi/attence?courseid=MDAwMDAwMDAwMLOcqZWH37Np'
    kq_res = HttpRequest().http_request(kq_url, {}, 'get', res.cookies)
    print("考勤的接口查询结果是{0}".format(kq_res.json()))
    # print("考勤的cookie{0}".format(kq_res.cookies))考勤接口没有cookies, 登录成功会返回cookies