# -*- coding:utf-8 -*-
# @Time : 2019-08-27
# @Author：lqc
# @Email:572948875@qq.com
# File : http_request.py

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

# register_url = "http://119.23.241.154:8080/fututeloan/mvc/api/member/register"
# register_data = {"mobilephone":"15096098888", "pwd":"123456"}
# # register_res = requests.get(register_url, register_data)
# # print("text解析的结果", register_res.text)
# # print("json解析的结果", register_res.json())
# #
# login_url = "http://119.23.241.154:8080/fututeloan/mvc/api/member/login"
# login_data = {"mobilephone":"15096098888", "pwd":"123456"}
# # login_res = requests.get(login_url, login_data)
# # print("text解析的结果", login_res.text)
# # print("json解析的结果", login_res.json())
# #
# recharge_url = "http://119.23.241.154:8080/fututeloan/mvc/api/member/login"
# recharge_data = {"mobilephone":"15096098888", "pwd":"123456"}
# # headers = {"User-Agent":"Mozilla/5.0"}
# # recharge_res = requests.get(recharge_url, recharge_data, cookies = login_res.cookies, headers = headers)
# # print("text解析的结果", recharge_res.text)
# # print("json解析的结果", recharge_res.json())
# # print("请求头:", recharge_res.request.headers)
# # print("响应头:", recharge_res.headers)

# cookie:会员卡，所有请求出自同一个客户端，同一个用户发起的请求
# session:保证会话的有效性，有效期间内进行的请求
# token:鉴权  防止非法访问，请求从哪个页面过来，请求不是非法的，是否来自合法的页面
# key:授权  拿到秘钥，才有权限访问页面、接口

# 拓展  get请求必须要指明params
# s = requests.session()  # 创建了一个会话
#  #  login_res = s.get(login_url, login_data)
# 会报错，参数多了
# login_res = s.get(login_url, params = login_data)
# recharge_res = s.post(recharge_url, recharge_data, cookies = login_res.cookies)
# recharge_res = s.post(recharge_url, recharge_data)  # 不传cookie也可以成功
# print("充值的结果是", recharge_res.json())
