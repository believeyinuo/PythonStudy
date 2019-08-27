# -*- coding:utf-8 -*-
# @Time : 2019-08-27
# @Author：lqc
# @Email:572948875@qq.com
# File : run.py

from PythonStudy.interface_auto_practice_50.tools.http_requester import HttpRequest
from PythonStudy.interface_auto_practice_50.tools.do_excel import DoExcel
from PythonStudy.interface_auto_practice_50.tools.get_cookie import GetCookie

COOKIE = None

# test_data = [{"url": "http://119.23.241.154:8080/fututeloan/mvc/api/member/login",
#               "data": {"mobilephone": "15096098888", "pwd": "123456"},
#               "title": "正常登陆", "http_method": "get"},
#              {"url": "http://119.23.241.154:8080/fututeloan/mvc/api/member/login",
#               "data": {"mobilephone": "15096098888", "pwd": "123456789"},
#               "title": "输入错误的密码登陆", "http_method": "get"}]
test_data = DoExcel().do_excel("test_data/interface_auto_pricatice.xlsx", "python")


def run(test_data):
    # global COOKIE
    for item in test_data:
        print("正在测试的用例是{0}".format(item["title"]))
        # res = HttpRequest().http_request(item["url"], item["data"], item["http_method"], COOKIE)
        res = HttpRequest().http_request(item["url"], item["data"], item["http_method"], getattr(GetCookie, "Cookie"))
        if res.cookies:
            setattr(GetCookie, "Cookie", res.cookies)
        #     COOKIE = res.cookies
        print("充值的结果：{}".format(res.json()))
        DoExcel().write_back(item["case_id"] + 1, str(res.json()))


run()
