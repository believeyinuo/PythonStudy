# -*- coding:utf-8 -*-
# @Time : 2019-09-15 19:27
# @Author：lqc
# @Email:572948875@qq.com
# File : dir_config.py

import os

# 框架项目顶层目录
base_dir = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]

testdatas_dir = os.path.join(base_dir, "TestDatas")

testcases_dir = os.path.join(base_dir, "TestCases")

htmlreport_dir = os.path.join(base_dir, "Outputs/reports")

logs_dir = os.path.join(base_dir, "Outputs/logs")

# config_dir = os.path.json(base_dir, "Config")

screenshoot_dir = os.path.join(base_dir, "Outputs/screenshots")