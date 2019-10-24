# -*- coding: utf-8 -*-
# @Time : 2019/10/22 8:31 下午
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : conftest.py
# @Project : PythonStudy

import pytest
from APP_AUTO_TEST.practice_126_5.Common.basepage import BasePage
import time
import yaml
from APP_AUTO_TEST.practice_126_5.Common.dir_config import caps_dir
from appium import webdriver
from APP_AUTO_TEST.practice_126_5.PageObjects.Comm_Business import CommonBus

# 登录用例使用的前置后置
@pytest.fixture
def startApp():
    # 准备服务器参数，与appium server进行连接。noReset=True
    driver = baseDriver()
    # 1、要不要判断欢迎页面是否存在？
    CommonBus(driver).do_welcome()
    # 2、要不要判断当前用户是否已登录？ -- 接口
    # 3、如果已登录，那么先退出.  -- 接口

# 除登录以外，通用的前置条件
@pytest.fixture()
def loginApp():
    # 准备服务器参数，与appium server进行连接。noReset=True
    driver = baseDriver()
    # 1、要不要判断欢迎页面是否存在？
    CommonBus(driver).do_welcome()
    # 2、判断是否已登录操作，若没有登录，则进行登录操作
    # 3、是否有设置手势密码的框。不设置

def baseDriver(server_port=4723, noReset=None, automationName=None, **kwags):
    # 将默认的配置数据读取出来
    fs = open(caps_dir + "/caps.yaml")
    desired_caps = yaml.load(fs)
    # 调整参数
    if noReset is not None:
        desired_caps["noReset"] = noReset
    if automationName is not None:
        desired_caps["automationName"] = automationName

    # kwargs

    # 返回一个启动对象 - driver
    drver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(server_port), desired_caps)