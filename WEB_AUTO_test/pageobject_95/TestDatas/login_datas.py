# -*- coding:utf-8 -*-
# @Time : 2019-09-14 20:32
# @Author：lqc
# @Email:572948875@qq.com
# File : login_datas.py

# 正常场景 - 测试数据
success_data = {"user":"18684720553", "password":"python"}

# 异常用例-手机号码格式不正确(大于11位、小于11位、为空、不在号码段)
phone_data = [{"user":"186847205533", "password":"python", "check":"请输入正确的手机号"},
              {"user":"186847205", "password":"python", "check":"请输入正确的手机号"},
              {"user":"", "password":"python", "check":"请输入手机号"},
              {"user":"11684720553", "password":"python", "check":"请输入正确的手机号"},
              {"user":"18684720553", "password":"", "check":"请输入密码"}]

# 异常用例