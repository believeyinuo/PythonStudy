# -*- coding: utf-8 -*-
# @Time : 2019-08-26 11:28
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : do_config.py
# @Project : PythonStudy

# 配置文件
# properties config ini log4j
# configparser读取配置信息

import configparser

# section option value

cf = configparser.ConfigParser()
cf.read("case.config", encoding='utf-8')

# 读取配置文件的数据
res_1 = cf.get("MODE", "mode")
print(res_1)

res_2 = cf["MODE"]["mode"]
print(res_2)

print(cf.sections())
print(cf.items("PYTHON11"))

# 数据类型的问题
print(type(cf.get("python11", "num")))