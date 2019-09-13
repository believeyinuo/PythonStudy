# -*- coding:utf-8 -*-
# @Time : 2019-09-13 21:11
# @Author：lqc
# @Email:572948875@qq.com
# File : 91_execute_script.py

# js处理滚动条、日期框

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

# 滚动条处理
# 1、找到要滚动到可视区域的元素
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//a[contains(text(), "5周年·遇见不一样的")]')))
ele = driver.find_element_by_xpath('//a[contains(text(), "5周年·遇见不一样的")]')

# 2、使用js进行滚动操作
driver.execute_script("arguments[0].scrollIntoView();", ele)

# js语句
js = 'ele = document.getElementById("train_date"); ele.readOnly = false; ele.value = "2018-12-30"; '
driver.execute_script(js)


