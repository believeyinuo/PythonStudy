# -*- coding: utf-8 -*-
# @Time : 2019/10/24 2:31 下午
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : Comm_Business.py
# @Project : PythonStudy

from APP_AUTO_TEST.practice_126_5.Common.basepage import BasePage
import time


class CommonBus(BasePage):
    # 欢迎页面
    # 处理欢迎页面
    def do_welcome(self):
        time.sleep(7)
        # 如果没有找到首页的元素/或者不包含MainActivity,那么就是在欢迎页面
        curAct = self.driver.current_activity
        if curAct.find("MainActivity") == -1:
            # 滑动欢迎页面至首页
            # 左滑3次点击立即体验
            for i in range(3):
                self.swipe_left(self.get_size())
                time.sleep(1)
            # 点击立即体验
            pass

# 导航栏

# 是否设置手势密码
    def is_setGesture(self, action=False):
        # 有没有设置手势密码的弹窗 - 5 秒
        # 如果有，是设置还是不设置呢？
        if action == False:
            pass # 点击不设置
        else:
            pass # 点击立即设置


