# -*- coding:utf-8 -*-
# @Time : 2019-09-15 13:01
# @Author：lqc
# @Email:572948875@qq.com
# File : user_page.py

from WEB_AUTO_test.pageobject_95.Common.basepage import BasePage
from WEB_AUTO_test.pageobject_95.PageLocators.user_page_locator import UserPageLocator as loc


class UserPage(BasePage):

    # 获取用户余额
    def get_user_leftMoney(self):
        doc = "个人页面_获取用户余额"
        # 等待元素
        self.wait_eleVisible(loc.user_leftMoney, doc=doc)
        # 获取个人可用余额的文本内容
        text = self.get_text(loc.user_leftMoney, doc)
        # 截取数字部分 - 分隔符为 元
        return text.strip("元")

    # 获取第一条投资记录的时间、投资金额、收益金额 -- 扩展
    # def get_first_investRecord_info(self):
    #     pass