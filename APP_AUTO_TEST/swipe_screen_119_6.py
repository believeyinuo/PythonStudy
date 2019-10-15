# -*- coding:utf-8 -*-
# @Time : 2019-10-15 21:36
# @Author：lqc
# @Email:572948875@qq.com
# File : swipe_screen_119_6.py

from appium import webdriver

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
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

loc = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("项目")')
WebDriverWait(driver, 30).until(EC.visibility_of_element_located(loc))
# height、width
size = driver.get_window_size()
start_X = size["width"] * 0.9
start_Y = size["height"] * 0.5
end_X = size["width"] * 0.1
end_Y = size["height"] * 0.5
# 从右向左滑
driver.swipe(start_X, start_Y, end_X, end_Y, 100)
time.sleep(1)
driver.swipe(start_X, start_Y, end_X, end_Y, 100)
# # 从左往右滑
# driver.swipe(end_X, end_Y, start_X, start_Y)
#
# # 上下滑动
# driver.swipe(size["width"] * 0.5, size["height"] * 0.9, size["width"] * 0.5, size["height"] * 0.1)
# driver.swipe(size["width"] * 0.5, size["height"] * 0.1, size["width"] * 0.5, size["height"] * 0.9)


