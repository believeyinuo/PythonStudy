# -*- coding: utf-8 -*-
# @Time : 2019/10/22 8:30 下午
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : basepage.py
# @Project : PythonStudy

import logging
import datetime
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
1、封装基本函数 - 执行日志、异常处理、失败截图
2、所有的页面公共的部分
"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 等待元素可见
    def wait_eleVisible(self, locator, wait_times=30, poll_frequency=0.5, doc=""):
        """
        :param locator: 元素定位。元素形式。（元素定位类型、元素定位方式）
        :param wait_times:
        :param poll_frequency:
        :param doc:模块名_页面名称_操作名称
        :return:
        """
        logging.info("等待元素 {0} 可见".format(locator))
        try:
            # 开始时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_times = (end - start).seconds
            logging.info("{0}：元素 {1} 已可见，等待起始时间：{2}，等待结束时间：{3}，等待时长：{4}".format())
