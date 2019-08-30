# -*- coding: utf-8 -*-
# @Time : 2019-08-28 13:40
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : project_path.py
# @Project : PythonStudy

# 专门来读取路径的值

import os
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 测试用例的路径
test_case_path = os.path.join(project_path,"test_data", "interface_auto_practice.xlsx")

# 测试报告的路径
test_report_path = os.path.join(project_path, "test_result", 'html_report', 'test_report.html')

# 配置文件的路径
case_config_path = os.path.join(project_path, "config", "case.config")
print(case_config_path)