# -*- coding:utf-8 -*-
# @Time : 2019-09-16 22:13
# @Author：lqc
# @Email:572948875@qq.com
# File : conftest.py

from selenium import webdriver
import pytest
from WEB_AUTO_test.pageobject_95.TestDatas import Common_Datas as CD
from WEB_AUTO_test.pageobject_95.PageObjects.login_page import LoginPage
import time

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
    time.sleep(0.5)

@pytest.fixture(scope="class")
def login_web():
    global driver
    # 前置操作
    print("=======所有测试用例之前的，setup===整个测试类只执行一次===")
    driver = webdriver.Chrome()
    driver.get(CD.web_login_url)
    LoginPage(driver).login(CD.user, CD.password)
    IndexPage(driver).click_first_bid()
    # yield 准备工作和清理工作的分界线。上面是准备工作，下面是清理工作
    # 有返回值得情况下，返回值写在yield后面。
    yield driver
    print("=========所有测试用例之后的，teardown===整个测试类只执行一次=====")
    driver.quit()

#@pytest.fixture(scope="session") # -s参数在控制台输出print内容
# def session_demo():
#   print("********我是整个测试会话周期的开始*****************")
#   yield
#   print("********我是整个测试会话周期的结束*****************")

#@pytest.fixture(scope="class")
# def class_demo():
#   print("********我是class的开始**********")
#   yield
#   print("********我是class的结束**********")

#@pytest.fixture
#def fuc_demo():
#   print("********我是function的开始**********")