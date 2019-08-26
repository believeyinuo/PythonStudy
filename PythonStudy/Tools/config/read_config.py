# -*- coding: utf-8 -*-
# @Time : 2019-08-26 11:45
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : read_config.py
# @Project : PythonStudy

import configparser


class ReadConfig:
    def read_config(self, file_name, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding="utf-8")
        return cf.get(section, option)
