# -*- coding: utf-8 -*-
# @Time : 2019-08-29 16:58
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : do_mysql.py
# @Project : API_AUTO_test

import pymysql
from PythonStudy.interface_auto_practice_50.tools import project_path
from PythonStudy.interface_auto_practice_50.tools.read_config import ReadConfig


class DoMysql:

    # query-->>查询语句  state-->> all 多条， 1 -->> 一条
    def do_mysql(self, query_sql, state = 'all'):

        # 从配置文件里面读取db info
        db_config = eval(ReadConfig().get_config(project_path.case_config_path, 'DB', 'db_config'))

        # 创建一个数据库连接
        con = pymysql.Connect(**db_config)

        # 游标
        cursor = con.cursor()

        # 执行语句
        cursor.execute(query_sql)

        # 获取结果  打印结果
        if state == 1:
            res = cursor.fetchone()
        else:
            res = cursor.fetchall()

        # 关闭游标
        cursor.close()

        # 关闭连接
        con.close()

        return res


if __name__ == '__main__':
    from PythonStudy.interface_auto_practice_50.tools import get_data
    query_sql = 'select max(id) from loan where MemberID = {0}'.format(getattr(GetData, 'loan_member_id'))
    print(DoMysql().do_mysql(query_sql, 1))
