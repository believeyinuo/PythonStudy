# -*- coding: utf-8 -*-
# @Time : 2019/10/24 11:52 上午
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : login_page.py
# @Project : PythonStudy

from APP_AUTO_TEST.practice_126_5.Common.basepage import BasePage
from APP_AUTO_TEST.practice_126_5.PageLocators.login_locators import LoginLocators as loc

class LoginPage(BasePage):

    # 登录操作
    def login_ussername(self, username):
        # 输入用户名
        # 输入密码
        doc = "登录页面_输入用户名页面"
        self.wait_eleVisible(loc.user_input, doc=doc)
        self.input_text(loc.user_input, doc=doc)
        # self.input_text(loc.passwd_input, passwd, doc)
        # 判断一下remeber_user的值。来决定是否勾选。
        self.click_element(loc.next_step, doc)

    def input_passwd(self, passwd):
        doc = "登录页面_输入密码页面"
        self.wait_eleVisible(loc.passwd_input, doc=doc)
        self.input_text(loc.passwd_input, passwd, doc)
        # self.input_text(loc.passwd_input, passwd, doc)
        # 判断一下remeber_user的值，来决定是否勾选
        self.click_element(loc.next_step, doc)

    def get_wrongMsg_from_userPage(self):
        pass

    def get_wrongMsg_from_passwdPage(self):
        pass


