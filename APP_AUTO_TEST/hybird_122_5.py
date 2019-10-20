# -*- coding:utf-8 -*-
# @Time : 2019-10-19 20:54
# @Author：lqc
# @Email:572948875@qq.com
# File : hybird_122_5.py


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
# 重置与否(
desired_caps["noReset"] = True

# 连接appium server。前提：appium desktop要启动。有监听端口
# 将desired_caps发送给appium server。打开app。
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

loc = 'new UISelector().text("全程班")'
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MobileBy.ANDROID_UIAUTOMATOR, loc)))
driver.find_element_by_android_uiautomator(loc).click()

# 等待webview元素出现
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MobileBy.CLASS_NAME, 'android.webkit.Webview')))
time.sleep(1)

# 前提：可以识别到webview  需要开启app的webview debug属性。
# context  # 原生控件   # webview
# 1、列出所有的context
cons = driver.contexts  # 列表
print(cons)

# 2、切换至webview，要确保chromedriver的版本要与webview的版本匹配。也要放置在对应的位置
driver.switch_to.context(cons[-1])

# 3、切换之后："当前的操作对象:html页面"----uc-devtool工具识别html页面，定位元素
# 等待元素可见
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((MobileBy.XPATH, "//button[@class='bottom-btn'")))
driver.find_element_by_xpath("//button[@class='bottom-btn'").click()