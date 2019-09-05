# -*- coding:utf-8 -*-
#@Time : 2019-09-04 
#@Author：lqc
#@Email:572948875@qq.com
#File : learn_web_driver.py

from selenium import webdriver

# 启动谷歌浏览器，开启与浏览器之间的会话   83讲的
# driver = webdriver.Chrome(service_log_path="/Users/LiQingChun/Desktop/logs")
driver = webdriver.Chrome()

# 访问一个网页
driver.get("https://www.baidu.com")

# 窗口最大化
driver.maximize_window()

driver.get("http://www.taobao.com")
# 回退上一页
driver.back()

# 前进到下一页
driver.forward()

# 刷新
driver.refresh()

# 获取标题
print(driver.title)

# 获取网址
print(driver.current_url)

# 窗口的句柄
print(driver.current_window_handle)

# 结束会话
# driver.quit()


