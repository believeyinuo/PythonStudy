# -*- coding:utf-8 -*-
# @Time : 2019-09-13 14:33
# @Author：lqc
# @Email:572948875@qq.com
# File : 90_mouse_select.py

from selenium.webdriver.common.action_chains import ActionChains
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

# 先找到鼠标要操作的元素
ele = driver.find_element_by_xpath('//*[@id="u1"]//a[@name="tj_settingicon"]')

# ele.click()
# # 2、实例化ActionChains类
# ac = ActionChains(driver)
#
# # 3、将鼠标操作添加到actions列表中
# ac.move_to_element(ele)
#
# # 4、调用perform()来执行鼠标操作
# ac.perform()
#
ActionChains(driver).move_to_element(ele).perform()

# 选择下拉列表当中的高级搜索
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH,'//a[text()="高级搜索"]')))
driver.find_element_by_xpath('//a[text()="高级搜索"]').click()

# select 类
from selenium.webdriver.support.ui import Select
# 1、找到select元素
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//select[@name="ft"]')))
select_ele = driver.find_element_by_xpath('//select[@name="ft"]')

# 2、实例化select类
s = Select(select_ele)

# 3、选择下拉列表值
# 方式一：下标从0开始
# s.select_by_index(4)
# 方式二：value值
# s.select_by_value("all")
# 方式三：文本内容
s.select_by_visible_text('Adobe Acrobat PDF (.pdf)')




