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
    app自动化：1）提供平台信息和app信息：平台版本、平台名称、设备名称、app包名、app入口activity
              2) 与appium服务进行连接，并发送平台和app信息

    toast信息：automationName = UiAutomator2
    noRest = True,False

    使用yaml来管理启动参数。
    定义basedriver函数，启动与app的会话。可以在basedriver中定制启动参数。

    考虑欢迎页面、登录成功、手势设置。
    原则：尽量不依赖app的状态和环境。在任何情况下，都是可以执行的。

待优化：
1、通过adb命令获取到当前连接的设备信息。平台版本、设备名称，设备id
   然后放到basedriver
2、多机并行并行。
    pytest 允许接收命令行的传参。pytest.main()
    一个appium server对应一台设备。
    五台设备 == 五个appium server。
    python的多线程
"""