# -*- coding:utf-8 -*-
# @Time : 2019-09-10 22:17
# @Author：lqc
# @Email:572948875@qq.com
# File : wait.py
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# 启动谷歌浏览器，开启与浏览器之间的会话
driver = webdriver.Chrome()

# 全局等待-隐形
# driver.implicitly_wait(30)

# 访问一个网页
driver.get("https://www.baidu.com")

driver.find_element_by_xpath('//*[@id="u1"]//a[@name="tj_login"]').click()

id = "TANGRAM__PSP_10__footerULoginBtn"
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, id)))

# 点击用户名密码登录
driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()

# 切换iframe = 进入了另外一个html
# 等待iframe存在，可见
driver.switch_to.frame("login_frame_qq")
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@name]="login_frame_qq"'))
time.sleep(0.5)
driver.find_element_by_id("switcher_plogin")

# 方式二：iframe切换
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it("login_frame_qq"))
time.sleep(0.5)

# 从iframe当中回到默认的页面当中
driver.switch_to.default_content()

driver.switch_to.parent_frame()
