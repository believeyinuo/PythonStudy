# -*- coding:utf-8 -*-
# @Time : 2019-09-12 22:59
# @Author：lqc
# @Email:572948875@qq.com
# File : alert_switch_89.py

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 启动谷歌浏览器，开启与浏览器之间的会话
driver = webdriver.Chrome()
driver.maximize_window()

# 全局等待-隐形
# driver.implicitly_wait(30)

# 访问一个网页
driver.get("")

# 等待alert出现
WebDriverWait(driver, 10).until(EC.alert_is_present())

# alert切换  不是html页面元素
alert = driver.switch_to.alert

# 打印弹出框的内容
print(alert.text)

# 关闭弹出框
alert.accept()
# alert.dismiss()