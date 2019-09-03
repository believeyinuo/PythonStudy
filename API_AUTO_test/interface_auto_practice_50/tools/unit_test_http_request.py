# -*- coding: utf-8 -*-
# @Time : 2019-08-28 10:42
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : unit_test_http_request.py
# @Project : API_AUTO_test

import unittest
from PythonStudy.interface_auto_practice_50.tools.http_request import HttpRequest
from PythonStudy.interface_auto_practice_50.tools.do_excel_old import DoExcel
from PythonStudy.interface_auto_practice_50.tools.get_data import GetData
from ddt import ddt, data  # 列表嵌套列表，列表嵌套字典
from PythonStudy.interface_auto_practice_50.tools.project_path import *
from PythonStudy.interface_auto_practice_50.tools.do_logging import MyLog
from PythonStudy.interface_auto_practice_50.tools.do_mysql import DoMysql

test_data = DoExcel(test_case_path).do_excel()


@ddt
class TestHttpRequest(unittest.TestCase):
    # def __init__(self, url, data, method, cookies, methodName):
    #     super(TestHttpRequest, self).__init__(methodName)
    #     self.url = url
    #     self.data = data
    #     self.method = method
    #     self.cookies = cookies

    @data(*test_data)
    def test_api(self, item):
        # 请求之前完成loan_id的替换
        MyLog().info("开始执行用例{0}:{1}".format(item['case_id'], item['title']))
        if item['data'].find('${loan_id}') != -1:
            if getattr(GetData, 'loan_id') == None:
                query_sql = 'select max(id) from loan where MemberID = {0}'.format(getattr(GetData, 'loan_member_id'))
                loan_id = DoMysql().do_mysql(query_sql)[0][0]
                item['data'] = item['data'].replace('${loan_id}', str(loan_id))
                setattr(GetData, 'loan_id', loan_id)  # 利用反射存储结果
                MyLog().info(loan_id)
            else:
                MyLog().info(getattr(GetData, 'loan_id'))
                item['data'] = item['data'].replace('${loan_id}', getattr(GetData, 'loan_id'))

        MyLog().info("获取到的请求数据是：{0}".format(item["data"]))
        MyLog().info("---------------开始http接口请求------------------")
        if item["check_sql"] != None:
            MyLog().info("词条用例需要做数据库校验:{0}".format(item["title"]))
            query_sql = eval(item["check_sql"])["sql"]
            before_amount = DoMysql().do_mysql(query_sql, 1)[0]
            MyLog().info("用例：{0}请求之前的余额是{1}".format(item["title"], before_amount))
            res = HttpRequest().http_request(item["url"], eval(item["data"]), item["method"], getattr(GetData, "Cookie"))

            MyLog().info("---------------完成http接口请求------------------")
            after_amount = DoMysql().do_mysql(query_sql, 1)[0]
            MyLog().info("用例：{0}请求之后的余额是{1}".format(item["title"], after_amount))

            # 检查结果
            if abs(after_amount - before_amount) == eval(item["data"]["amount"]):
                MyLog.info("数据库余额校验通过")
                check_sql_result = '数据库检查通过'
            else:
                MyLog.info("数据库余额校验通过")
                check_sql_result = '数据库检查通过'
            DoExcel().write_back(test_case_path, item["sheet_name"], item["case_id"] + 1, 10, check_sql_result)
        else:
            res = HttpRequest().http_request(item["url"], eval(item["data"]), item["method"], getattr(GetData, "Cookie"))

            MyLog().info("---------------完成http接口请求------------------")


        if res.cookies:
            setattr(GetData, "Cookie", res.cookies)
        try:
            self.assertEqual(str(item["expected"]), res.json()['code'])
            TestResult = 'PASS'
        except AssertionError as e:
            MyLog().info("执行用例出错：{0}".format(e))
            TestResult = 'Failed'
            raise e
        finally:
            DoExcel.write_back(test_case_path, item["sheet_name"], item["case_id"] + 1, 8, res.text)
            DoExcel.write_back(test_case_path, item["sheet_name"], item["case_id"] + 1, 9, TestResult)
            MyLog().error("获取到的结果是：{0}".format(res.json()))
        return res
