# -*- coding:utf-8 -*-
# @Time : 2019-09-15 16:19
# @Author：lqc
# @Email:572948875@qq.com
# File : index_page_locators.py

from selenium.webdriver.common.by import By


class IndexPageLocators:
    # 用户昵称
    user_link = (By.XPATH, 'a[@href="/Member/index.html"]')
    # 抢投标按钮
    bid_button = (By.XPATH, 'a[@class="btn btn-special"]')