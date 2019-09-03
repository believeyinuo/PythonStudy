# -*- coding:utf-8 -*-
#@Time : 2019-08-21 
#@Author：lqc
#@Email:572948875@qq.com
#File : http_request.py

import requests

# url = "http://120.78.128.25:8765/Index/login.html"
# res = requests.get(url)#返回一个消息实体
# print(res)
# #响应头  响应状态码  响应报文
# print("响应头：",res.headers);
# print("响应状态码", res.status_code);
# print("响应正文：", res.text)#html xml json

#post请求
url = "http://119.23.241.154:8080/futureloan/mvc/api/member/login"
data = {"mobilephone":"1509609550", "pwd":"123456"}
res = requests.post(url, data)
# #响应头  响应状态码  响应报文
print("响应头：",res.headers);
print("响应状态码", res.status_code);
print("响应正文：", res.text)#html xml json  字符串形式
print("响应正文：", res.json())#字典形式
print("cookies:", res.cookies)
print("请求头", res.request.headers)

