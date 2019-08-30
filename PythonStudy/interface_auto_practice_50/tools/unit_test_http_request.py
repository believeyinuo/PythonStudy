# -*- coding: utf-8 -*-
# @Time : 2019-08-28 10:42
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : unit_test_http_request.py
# @Project : PythonStudy

import unittest
from PythonStudy.interface_auto_practice_50.tools.http_request import HttpRequest
from PythonStudy.interface_auto_practice_50.tools.do_excel import DoExcel
from PythonStudy.interface_auto_practice_50.tools.get_data import GetData
from ddt import ddt, data  # 列表嵌套列表，列表嵌套字典
from PythonStudy.interface_auto_practice_50.tools.project_path import *
from PythonStudy.interface_auto_practice_50.tools.do_logging import MyLog
from PythonStudy.interface_auto_practice_50.tools.do_mysql import DoMysql

test_data = DoExcel(test_case_path, "login").do_excel()


@ddt
class TestHttpRequest(unittest.TestCase):
    # def __init__(self, url, data, method, cookies, methodName):
    #     super(TestHttpRequest, self).__init__(methodName)
    #     self.url = url
    #     self.data = data
    #     self.method = method
    #     self.cookies = cookies

    @data(*test_data)
    def test_http_request(self, item):
        # 请求之前完成loan_id的替换
        MyLog().info("开始执行用例{0}:{1}".format(item['case_id'], item['title']))
        if item['data'].find('${loan_id}') != -1:
            if getattr(GetData, 'loan_id') != -1:
                query_sql = 'select max(id) from loan where MemberID = {0}'.format(getattr(GetData, 'loan_member_id'))
                loan_id = DoMysql().do_mysql(query_sql)[0][0]
                item['data'] = item['data'].replace('${loan_id}', str(loan_id))
                setattr(GetData, 'loan_id', loan_id)  # 利用反射存储结果
            else:
                item['data'] = item['data'].replace('${loan_id}', getattr(GetData, 'loan_id'))


        res = HttpRequest().http_request(item["url"], eval(item["data"]), item["method"], getattr(GetData, "Cookie"))
        if res.cookies:
            setattr(GetData, "Cookie", res.cookies)
        try:
            self.assertEqual(str(item["expected"]), res.json()['code'])
            TestResult = 'PASS'
        except AssertionError as e:
            MyLog().info("断言错误{0}".format(e))
            TestResult = 'Failed'
            raise e
        finally:
            DoExcel.write_back(test_case_path, item["sheet_name"], item["case_id"] + 1, res.text, TestResult)
            MyLog().error("获取到的结果是：{0}".format(res.json()))

        return res
