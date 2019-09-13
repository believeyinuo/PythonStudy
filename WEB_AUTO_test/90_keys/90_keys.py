# -*- coding:utf-8 -*-
# @Time : 2019-09-13 18:51
# @Author：lqc
# @Email:572948875@qq.com
# File : 90_keys.py

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 启动谷歌浏览器，开启与浏览器之间的会话
driver = webdriver.Chrome()
driver.maximize_window()

driver.find_element_by_xpath("").send_keys(Keys.ENTER, 'a')

# 获取文本内容
driver.find_element_by_xpath("").text()
# 获取属性
driver.find_element_by_xpath("").get_attribute("style")