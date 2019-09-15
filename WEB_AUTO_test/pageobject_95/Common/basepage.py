# -*- coding:utf-8 -*-
# @Time : 2019-09-15 17:07
# @Author：lqc
# @Email:572948875@qq.com
# File : basepage.py

# 1、封装基本函数 - 执行日志、异常处理、失败截图
# 2、所有的页面公共的部分

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from WEB_AUTO_test.pageobject_95.Common import dir_config

import logging
import datetime

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        
    # 等待元素可见
    def wait_eleVisible(self, locator, wait_times = 30, poll_frequency = 0.5, doc=""):
        """
        :param locator: 元素定位，元组形式（元素定位类型、元素定位方式）
        :param times:
        :param poll_frequency:
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        logging.info("等待元素 {0} 可见".format(locator))
        try:
            # 开始等待的时间
            start = datetime.datetime.now()
            WebDriverWait(self.driver, wait_times, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待的时间
            end = datetime.datetime.now()
            # 求一个差值，写在日志中，等待了多久
            wait_times = (end - start).seconds
            logging.info("{0}：元素 {1} 已可见，等待起始时间：{2}，等待结束时间：{3}, 等待时长为{4}", format(doc, locator, start, end, wait_times))
        except:
            logging.exception("等待元素可见异常！！！")
            # 截图
            self.save_scrren_shoot(doc)
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
            # 截图
            self.save_scrren_shoot(doc)
            raise

    def get_elements(self, locator, doc=""):
        # 查找元素
        logging.info("{0}：开始查找符合表达式的所有元素：{1}".format(doc, locator))
        try:
            return self.driver.find_elements(*locator)
        except:
            logging.exception("查找元素失败")
            self.save_scrren_shoot(doc)
            raise
    
    # 点击操作
    def click_element(self, locator, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 元素操作
        logging.info("{0} 点击元素:{1}".format(doc, locator))
        try:
            ele.click()
        except:
            logging.exception("元素点击操作失败！！！")
            # 截图
            self.save_scrren_shoot(doc)
            raise
    
    # 输入操作
    def input_text(self, locator, text, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        # 输入操作
        logging.info("{0}：元素：{1} 输入内容：{2}".format(doc, locator, text))
        try:
            ele.send_keys(text)
        except:
            logging.exception("元素输入操作失败！！！")
            # 截图
            self.save_scrren_shoot(doc)
            raise
    
    # 获取元素的文本内容
    def get_text(self, locator, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        logging.info("{0}：获取元素：{1} 的文本内容".format(doc, locator))
        try:
            text = ele.text
            logging.info("元素：{0} 的文本内容为: {1}".format(locator, text))
            return text
        except:
            logging.exception("获取元素文本失败！！！")
            # 截图
            self.save_scrren_shoot(doc)
            raise

    # 获取元素的属性
    def get_element_attribute(self, locator, attr, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        logging.info("{0}: 获取元素：{1} 的属性：{2}".format(doc, locator, attr))
        try:
            ele_attr = ele.get_attribute(attr)
            logging.info("元素：{0} 的属性 {1} 值为：{2}".format(locator, attr, ele_attr))
            return ele_attr
        except:
            logging.exception("获取元素的属性失败！！！")
            # 截图
            self.save_scrren_shoot(doc)
            raise

    # 元素存在则为True，否则为False
    def is_eleExist(self, locator, timeout = 10, doc=""):
        logging.info("在页面 {0} 中是否存在元素：{1}".format(doc, locator))
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            logging.info(" {0} 秒内页面 {1} 中存在元素：{2}".format(timeout, doc, locator))
            return True
        except:
            logging.info(" {0} 秒内页面 {1} 中不存在元素：{2}".format(timeout, doc, locator))
            return False
    
    # alert处理
    def alert_action(self, action = "accept"):
        pass
    
    # iframe处理
    def switch_iframe(self):
        pass
    
    # 上传操作
    def upload_file(self):
        pass

    # 滚动条处理
    # 窗口切换

    def save_scrren_shoot(self, doc):
        # 图片名称：模块名称_页面名称_操作名称_年-月-日_时—分-秒.png
        # filepath=值得图片保存目录/model(页面功能名称)_当前时间到秒.png
        filepath = dir_config.screenshot_dir + \
                   "/{0}_{1}.png".format(doc, time.strftime("%Y-%m-%d-%H-%M-%s", time.localtime()))
        # 截图文件存放在 Screenshot 目录下
        # driver方法：self.driver.save_screenshot()
        try:
            self.driver.save_screenshoot(filepath)
            logging.info("截屏成功，图片路径为:{}".format(filepath))
        except:
            logging.exception("截图失败")