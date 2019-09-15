# -*- coding:utf-8 -*-
# @Time : 2019-09-15 13:01
# @Author：lqc
# @Email:572948875@qq.com
# File : bid_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
from WEB_AUTO_test.pageobject_95.PageLocators.bid_page_locators import BidPageLocators as loc
from WEB_AUTO_test.pageobject_95.Common.basepage import BasePage


class BidPage(BasePage):

    # 投资
    def invest(self, money):
        # 在输入框中输入金额
        doc = "标详情页面_投资操作"
        self.wait_eleVisible(loc.money_input, doc)
        # WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.money_input))
        self.input_text(loc.money_input, money, doc)
        # self.driver.find_element(*loc.money_input).send_keys(money)
        # 点击投标按钮
        self.click_element(loc.invest_button, doc)
        # self.driver.find_element(*loc.invest_button).click()

    # 获取用户余额
    def get_user_money(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.money_input))
        return self.driver.find_element(*loc.money_input).get_attribute("data-amount")

    # 投资成功的提示框-点击查看并激活
    def click_activeButton_on_success_popup(self):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.active_button_on_successPop))
        self.driver.find_element(*loc.active_button_on_successPop).click()

    # 错误提示框-页面中间
    def get_errorMsg_from_pageCenter(self):
        # 获取文本内容
        # 关闭弹出框
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(loc.invest_failed_popup))
        msg = self.driver.find_element(*loc.invest_failed_popup).text
        # 关闭弹出框
        self.driver.find_element(*loc.invest_close_failed_popup_button).click()
        return msg

    # 获取提示信息-投标按钮上的
    def get_errorMsg_from_investButton(self):
        pass







