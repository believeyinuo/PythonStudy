# -*- coding: utf-8 -*-
# @Time : 2019-08-28 16:32
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : read_config.py
# @Project : API_AUTO_test

import configparser


class ReadConfig:

    @staticmethod
    def get_config(file_path, section, option):
        cf = configparser.ConfigParser()
        cf.read(file_path)
        return cf[section][option]

if __name__ == "__main__":
    from PythonStudy.interface_auto_practice_50.tools import project_path
    print(ReadConfig.get_config(project_path.case_config_path, 'MODE', 'mode'))