# -*- coding:utf-8 -*-
# @Time : 2019-09-16 22:13
# @Author：lqc
# @Email:572948875@qq.com
# File : conftest.py

from selenium import webdriver
import pytest
from WEB_AUTO_test.pageobject_95.TestDatas import Common_Datas as CD
from WEB_AUTO_test.pageobject_95.PageObjects.login_page import LoginPage

driver = None
# 声明它是一个fixture
@pytest.fixture(scope="class")
def access_web():
    global driver
    # 前置操作
    print("========所有测试用例之前的，setup============整个测试类只执行一次========")
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    lg = LoginPage(driver)
    yield (driver, lg)   # 分割线  # 后面接返回值
    # 后置操作
    print("========所有测试用例之后的，tearDown============整个测试类只执行一次========")
    driver.quit()

@pytest.fixture
def refresh_page():
    global driver
    # 前置操作
    yield
    # 后置操作
    driver.refresh()