# -*- coding: utf-8 -*-
# @Time : 2019-08-29 16:58
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : do_mysql.py
# @Project : PythonStudy

import pymysql

config = {'host':'119.23.241.154',
          'user':'python',
          'password':'python666',
          'port':3306

}
# 创建一个数据库连接
con = pymysql.Connect()

# 关键字参数的传递
