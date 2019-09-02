# -*- coding: utf-8 -*-
# @Time : 2019-09-02 17:56
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : learning_zhengze.py
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
s = 'ww.lemfix.com'  # 目标字符串
res = re.match('www', s)  # 全匹配  头部匹配
print(res.group(0))