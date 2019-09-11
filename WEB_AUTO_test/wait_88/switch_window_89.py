# -*- coding:utf-8 -*-
# @Time : 2019-09-11 23:00
# @Author：lqc
# @Email:572948875@qq.com
# File : switch_window_89.py
import time

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
driver.get("https://www.baidu.com")

#
driver.find_element_by_id("kw").send_keys("柠檬班")
driver.find_element_by_id("su").click()
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "吧_百度贴吧")]')))
driver.find_element_by_xpath('//a[contains(text(), "吧_百度贴吧")]').click()

time.sleep(0.5)


# 切换二：窗口切换
# step1:获取窗口的总数以及句柄，新打开的窗口位于最后一个
handles = driver.window_handles
print(handles)

# 当前窗口的句柄
print(driver.current_window_handle)

# step2:切换
driver.switch_to.window(handles[-1])

# 新的窗口页面操作
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "j_head_focus_btn")))
driver.find_element_by_id("j_head_focus_btn").click()

# 新的窗口是否打开
EC.new_window_is_opened