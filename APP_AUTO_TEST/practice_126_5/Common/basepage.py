# -*- coding: utf-8 -*-
# @Time : 2019/10/22 8:30 下午
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : basepage.py
# @Project : PythonStudy

import logging
import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from APP_AUTO_TEST.practice_126_5.Common import dir_config

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
            logging.info("{0}：元素 {1} 已可见，等待起始时间：{2}，等待结束时间：{3}，等待时长：{4}".format(doc, locator, start, end, wait_times))
        except:
            # 捕获异常到日志中：
            logging.exception("等待元素可见异常")
            # 截图 - 保存到指定的目录。名字要想好怎么取？
            self.save_screenshot(doc)
            # 抛出异常
            raise

    # 等待元素存在
    def wait_elePresence(self):
        pass

    # 查找元素
    def get_element(self, locator, doc=""):
        logging.info("{0} 查找元素：{1}".format(doc, locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败！！！")
            #截图
            self.save_screenshot(doc)
            raise

    def get_elements(self, locator, doc=""):
        # 查找元素
        logging.info("{0}:开始查找符合表达式的所有元素：{1}".format(doc, locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败。")
            self.save_screenshot(doc)
            raise

    # 点击操作
    def click_element(self, locator, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 元素操作
        logging.info("{0} 点击元素：{1}".format(doc, locator))
        try:
            ele.click()
        except:
            logging.exception("元素点击操作失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 输入操作
    def input_text(self, locator, text, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        


