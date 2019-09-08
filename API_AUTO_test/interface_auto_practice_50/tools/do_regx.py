# -*- coding:utf-8 -*-
# @Time : 2019-09-02
# @Author：lqc
# @Email:572948875@qq.com
# File : do_regx.py

import re
from API_AUTO_test.interface_auto_practice_50.tools.get_data import GetData


class DoRegx:

    @staticmethod
    def do_regx(s):
        while re.search('\$\{(.*?)\}', s):
            key = re.search('\$\{(.*?)\}', s).group(0)
            value = re.search('\$\{(.*?)\}', s).group(1)
            s = s.replace(key, str(getattr(GetData, value)))
        return s
