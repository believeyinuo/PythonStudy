# -*- coding:utf-8 -*-
# @Time : 2019-08-27
# @Author：lqc
# @Email:572948875@qq.com
# File : get_data.py

from PythonStudy.interface_auto_practice_50.tools import project_path
import pandas as pd
from PythonStudy.interface_auto_practice_50.tools.read_config import ReadConfig


class GetData:
    Cookie = None
    loan_id = None
    check_list = eval(ReadConfig.get_config(project_path.case_config_path, 'CHECKLEAVEAMOUNT', 'check_list'))
    NoRegTel = pd.read_excel(project_path.test_case_path, sheet_name='init').ix[0, 0]
    normal_tel = pd.read_excel(project_path.test_case_path, sheet_name='init').ix[1, 0]
    admin_tel = pd.read_excel(project_path.test_case_path, sheet_name='init').ix[2, 0]
    loan_member_id = pd.read_excel(project_path.test_case_path, sheet_name='init').ix[3, 0]
    member_id = pd.read_excel(project_path.test_case_path, sheet_name='init').ix[4, 0]

# setattr(GetCookie, "Cookie", "123456")  # set attribute 设置属性值
# hasattr(GetCookie, "Cookie")  # has attribute 判断是否有这个属性值
# getattr(GetCookie, "Cookie")  # get attribute 获取属性值
# delattr(GetCookie, "Cookie")  # delete attribute 删除这个属性
