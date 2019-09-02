# -*- coding: utf-8 -*-
# @Time : 2019-09-02 17:56
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : learning_regx.py
# @Project : PythonStudy

# 用一个规则匹配你想要的信息  正则表达式：元字符+限定符
# 元字符  限定符
#
# 元字符   意义                  限定符               意义
# .       任意单个字符             +                 匹配至少大于1次
# \d      任意单个数字             ?                 匹配0次或1次
#[0-9]    等价0-9                 *                匹配0次或多次  贪婪匹配
#[a-zA-Z] 等价所有的大小写字母       {n,}、{n,m}、{n}  匹配限定次数

import re
# s = 'www.lemfix.com'  # 目标字符串
# res = re.match('(w)(ww)', s)  # 全匹配  头部匹配
# print(res.group(0))  # group()==group(0) 拿到匹配的全部字符 分组  根据正则表达式里面的括号去分组

# s = 'hellolemonfixlemon'
# res = re.findall('(le)(mon)', s)  # 列表 在字符串里面找匹配的内容
# # 如果有分组 就是一元组的形式表现出来，列表嵌套元组
# print(res)
from PythonStudy.interface_auto_practice_50.tools.get_data import GetData
s = '{"mobilephone":"${normal_tel}", "pwd":"${pwd}"}'
while re.search('\$\{(.*?)\}', s):
    key = re.search('\$\{(.*?)\}', s).group(0)
    value = re.search('\$\{(.*?)\}', s).group(1)
    s = s.replace(key, str(getattr(GetData, value)))
    print(key, value)
    print(s)