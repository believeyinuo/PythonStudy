# -*- coding:utf-8 -*-
# @Time : 2019-09-15 11:20
# @Author：lqc
# @Email:572948875@qq.com
# File : login_page_locators.py

from selenium.webdriver.common.by import By

class LoginPageLocator:

    # 元素定位
    # 用户名输入框
    user_input = (By.XPATH, '//input[@name="phone"]')
    # 密码输入框
    pwd_input = (By.XPATH, '//input[@name="password"]')
    # 登录按钮
    login_but = (By.XPATH, '//button[text()="登录"]')
    # 错误提示框-登录区域
    errorMsg_from_loginArea = (By.XPATH, '//div[@class="form-error-info"]')
    # 登录页面_获取页面正中间错误信息
    pageCenter_error_info = (By.XPATH, '//div[@class ="layui-layer-content"]')