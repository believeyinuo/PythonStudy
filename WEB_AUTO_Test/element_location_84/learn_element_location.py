# -*- coding:utf-8 -*-
#@Time : 2019-09-05 
#@Author：lqc
#@Email:572948875@qq.com
#File : learn_element_location.py

# 元素定位
# id、classname、tagname、name

from selenium import webdriver

# 启动谷歌浏览器，开启与浏览器之间的会话
driver = webdriver.Chrome()

# 访问一个网页
driver.get("https://www.baidu.com")

# 方式一
ele = driver.find_element_by_id("kw")
print(ele.get_attribute("class"))
print(ele)

# 方式二
eles = driver.find_elements_by_class_name("s_ipt")
driver.find_element_by_class_name("s_ipt")

# 方式三
driver.find_element_by_name("wd")
driver.find_elements_by_name("wd")

# 方式四
driver.find_element_by_tag_name("input")
driver.find_elements_by_tag_name("input")

# 方式五、六 针对链接
driver.find_element_by_link_text("更多产品")
driver.find_elements_by_link_text("更多产品")
driver.find_element_by_partial_link_text("更多产品")
driver.find_elements_by_partial_link_text("更多产品")

# xpath
# driver.find_element_by_xpath("")
# 绝对定位
#      /html/body/div[2]/div/form/div[1]/input
#      以/开头
#      非常依赖于页面的顺序和位置
# 相对定位
#       //*[@id="kw"]
#       以//开头
#       不依赖页面的的顺序和位置。只看整个页面当中有没有符合表达式的元素
#       //标签名称[@属性名称=值]
#       逻辑运算  and or //标签名称[@属性名称=值 and @属性名称=值]
#       层级定位
#       //*[@id="third-nav"]//a[text()="资料"]
#       //a[text()="资料"]
#       //input[contains(@class, "username")
#       text()  文本定位
#       contains(@属性名称/text(), 文本内容)  包含

