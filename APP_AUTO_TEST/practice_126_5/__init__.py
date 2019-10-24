# -*- coding: utf-8 -*-
# @Time : 2019/10/22 8:23 下午
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : __init__.py.py
# @Project : PythonStudy

"""
1、bannerpage把它拿过来，直接用，新增了移动端的方法：滑屏/toast获取/h5切换
2、元素定位方式不同。新增了移动端的定位方式
    pageLocators 全部换成移动端的定位

    屏幕小、页面布局，页面功能有差异。页面会变多。
    PageObjects当中页面的功能，换成移动端的。
    页面划分的时候：登录页面-2个页面  考虑页面划分。

3、会话的启动方式：
    web自动化：webdriver.Chrome()
    app自动化：1）提供平台信息和app信息：平台版本、平台名称、设备名称、appbao'ming
"""