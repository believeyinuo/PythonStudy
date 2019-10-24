# -*- coding: utf-8 -*-
# @Time : 2019/10/24 2:48 下午
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : index_page.py
# @Project : PythonStudy

from APP_AUTO_TEST.practice_126_5.Common.basepage import BasePage

class IndexPage:

    def get_loginStatus(driver):
        # 获取当前app的登录状态。已登录为True,未登录为False
        try:
            # 等待5秒
            # 找登录/注册按钮
            return False
        except:
            return True