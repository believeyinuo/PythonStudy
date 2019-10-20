# -*- coding:utf-8 -*-
# @Time : 2019-10-16 21:14
# @Author：lqc
# @Email:572948875@qq.com
# File : touch_screen_119_11.py

from appium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
import time

desired_caps = {}
# 平台类型
desired_caps["platform"] = "Android"
# 平台版本号
desired_caps["platformVersion"] = "7.1"
# 设备名称
desired_caps["deviceName"] = "Android Emulator"
# app包名
desired_caps["appPackage"] = "cn.dagongniu.code"
# app入口activity
desired_caps["appActivity"] = "cn.dagongniu.oax.main.SplashActivity"
# 重置与否
desired_caps["noReset"] = True

# 连接appium server。前提：appium desktop要启动。有监听端口
# 将desired_caps发送给appium server。打开app。
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

ele = driver.find_element_by_id("")
# 元素的大小
size = ele.size
# 均分的步长 高和宽一样
step = size["width"] / 6
# 元素的起点坐标 - 左上角
ori = ele.location
point1 = (ori["x"] + step, ori["y"] + step)
point2 = (ori["x"] + 3 * step, ori["y"] + step)
point3 = (ori["x"] + 5 * step, ori["y"] + step)
point4 = (ori["x"] + 3 * step, ori["y"] + 3 * step)
point5 = (ori["x"] + 3 * step, ori["y"] + 5 * step)

TouchAction(driver).press(x=point1[0], y=point1[1]).wait(200). \
    move_to(x=point2[0], y=point2[1]).wait(200). \
    move_to(x=point3[0], y=point3[1]).wait(200). \
    move_to(x=point4[0], y=point4[1]).wait(200). \
    move_to(x=point5[0], y=point5[1]).wait(200). \
    release(). \
    perform()
