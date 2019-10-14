# -*- coding:utf-8 -*-
# @Time : 2019-10-11 21:27
# @Author：lqc
# @Email:572948875@qq.com
# File : demo_113_5.py

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

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

# 连接appium server。前提：appium desktop要启动。有监听端口
# 将desired_caps发送给appium server。打开app。
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

# 运行代码之前：1、appium server启动成功，处于监听状态
# 2、模拟器/真机必须能够被电脑识别。即adb devices能够识别到要操作的设备。

# id
driver.find_element_by_id("com.lemon.lemonban:id/navigation_tiku")
# class
driver.find_element_by_class_name("android.widget.FrameLayout")
# content-desc
driver.find_element_by_accessibility_id("")
# uiautomator
driver.find_element_by_android_uiautomator()