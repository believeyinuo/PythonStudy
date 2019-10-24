# -*- coding: utf-8 -*-
# @Time : 2019/10/22 8:31 下午
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : conftest.py
# @Project : PythonStudy

import pytest
from APP_AUTO_TEST.practice_126_5.Common.basepage import BasePage
import time


# 登录用例使用的前置后置
@pytest.fixture
def startApp():
    # 准备服务器参数，与appium server进行连接。noReset=True
    # 1、要不要判断欢迎页面是否存在？
    do_welcome()
    # 2、要不要判断当前用户是否已登录？ -- 接口
    # 3、如果已登录，那么先退出.  -- 接口



# 处理欢迎页面
def do_welcome(driver):
    # 如果没有找到首页的元素/或者不包含MainActivity,那么就是在欢迎页面
    curAct = driver.current_activity
    if curAct.find("MainActivity") == -1:
        # 滑动欢迎页面至首页
        # 左滑3次点击立即体验
        size = BasePage(driver).get_size()
        for i in range(3):
            BasePage(driver).swipe_left(size)
            time.sleep(1)
        # 点击立即体验
        pass
