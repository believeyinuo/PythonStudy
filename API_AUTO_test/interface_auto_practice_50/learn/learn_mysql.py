# -*- coding: utf-8 -*-
# @Time : 2019-08-30 11:00
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : learn_mysql.py
# @Project : API_AUTO_test

import pymysql

db_config = {'host':'47.107.168.87',
          'user':'python',
          'password':'python666',
          'port':3306,
          'database':'future'
}
# 创建一个数据库连接
con = pymysql.Connect(**db_config)

# 游标cursor
cursor = con.cursor()

# 写sql--字符串
query_sql = 'select max(MobilePhone) from member'

# 执行语句
cursor.execute(query_sql)


# 获取结果  打印结果
res = cursor.fetchone()  # 元组 针对一条数据
# res = cursor.fetchall()  # 列表 针对多行数据  列表嵌套元组
print(res)

# 关闭游标
cursor.close()

# 关闭连接
con.close()