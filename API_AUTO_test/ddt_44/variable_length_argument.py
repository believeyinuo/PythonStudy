# -*- coding: utf-8 -*-
# @Time : 2019-08-26 10:21
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : variable_length_argument.py
# @Project : API_AUTO_test

def print_msg(*args):
    print(args)

t = [1, 4]
print(*t)  # 脱外套
