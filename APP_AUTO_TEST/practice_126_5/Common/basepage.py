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
from appium.webdriver.common.mobileby import MobileBy

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
        # 输入操作
        logging.info("{0}：元素：{1}输入内容：{2}".format(doc, locator, text))
        try:
            ele.send_keys(text)
        except:
            logging.exception("元素输入操作失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素的文本内容
    def get_text(self, locator, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        logging.info("{0}：获取元素：{1} 的文本内容".format(doc, locator))
        try:
            text = ele.text
            logging.info("元素：{0} 的文本内容为：{1}".format(locator, text))
            return text
        except:
            logging.exception("获取元素文本内容失败！！！")
            # 截图
            self.save_screenshot(doc)
            raise

    # 获取元素的属性
    def get_element_attribute(self, locator, attr, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        logging.info("{0}：获取元素：{1}的属性：{2}".format(doc, locator, attr))
        try:
            ele_attr = ele.get_attribute(attr)
            logging.info("元素：{0} 的属性{1} 的值为：{2}".format(locator, attr, ele_attr))
            return ele_attr
        except:
            logging.exception("获取元素的属性失败！！！")
            # 截图
            self.save_screenshot(doc)

    # 元素存在则为True，否则为False
    def is_eleExist(self, locator, timeout=10, doc=""):
        logging.info("在页面 {0} 中是否存在元素：{1}".format(doc, locator))
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            logging.info("{0} 秒内页面 {1} 中存在元素：{2}".format(timeout, doc, locator))
            return True
        except:
            logging.info("{0} 秒内页面 {1} 中不存在元素：{2}".format(timeout, doc, locator))
            return False

    # 上下左右滑动
    def swipe_up(self, size):
        pass

    def swipe_down(self, size):
        pass

    def swipe_left(self, size):
        self.driver.swipe(size["width"] * 0.9, size["height"] * 0.5, size["width"] * 0.1, size["height"] * 0.5)
        pass

    def swipe_right(self, size):
        pass

    # 获取整个屏幕大小
    def get_size(self):
        return self.driver.get_windor_size()

    # toast获取
    def get_toastMsg(self, str):
        # 1、xpath表达式  文本匹配
        loc = '//*[contains(@text, "{}")]'.format(str)

        # 等待的时候，要用元素存在的条件。不能用元素可见的条件
        try:
            WebDriverWait(self.driver, 10, 0.01).until(EC.presence_of_element_located(MobileBy.XPATH, loc))
            return self.driver.find_element_by_xpath(loc).text
        except:
            logging.exception("没有找到匹配的toast!!!!")
            raise

    # h5切换

    def save_screenshot(self, doc):
        # 图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
        # filepath=指的图片保存目录/model(页面功能名称)_当前时间到秒.png
        filePath = dir_config.screenshot_dir + \
            "/{0}_{1}.png".format(doc, time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))
        # 截图文件存放在Screenshot目录下
        # driver方法：self.driver.save_screenshot()
        try:
            self.driver.save_screenshot(filePath)
            logging.info("截屏成功。图片路径为{}0".format(filePath))
        except:
            logging.exception("截图失败")


