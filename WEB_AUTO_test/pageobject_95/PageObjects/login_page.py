# -*- coding:utf-8 -*-
# @Time : 2019-09-14 18:40
# @Author：lqc
# @Email:572948875@qq.com
# File : login_page.py

from WEB_AUTO_test.pageobject_95.PageLocators.login_page_locators import LoginPageLocator as loc
from WEB_AUTO_test.pageobject_95.Common.basepage import BasePage


class LoginPage(BasePage):

    # 登录操作
    def login(self, username, password, remeber_user=False):
        # 输入用户名
        # 输入密码
        # 点击登录
        doc = "登录页面_登录功能"
        self.wait_eleVisible(loc.user_input, doc=doc)
        # WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.name_text))
        self.input_text(loc.user_input, username, doc)
        # self.driver.find_element(*loc.user_input).send_keys(username)
        self.input_text(loc.pwd_input, password, doc)
        # self.driver.find_element(*loc.pwd_input).send_keys(password)
        # 判断用一下remeber_user的值，来决定是否勾选
        self.click_element(loc.login_but, doc)
        # self.driver.find_element(*loc.login_but).click()

    # 注册入口
    # def register_enter(self):
    #     WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "")))
    #     self.driver.find_element_by_xpath("").click()

    # 忘记密码
    def forgetPwd(self):
        pass

    # 获取错误提示信息-登录区域
    def get_errorMsg_from_loginArea(self):
        doc = "登录页面_获取登录区域的错误提示"
        self.wait_eleVisible(loc.errorMsg_from_loginArea, doc=doc)
        # WebDriverWait(self.driver, 20).until(
        #     EC.visibility_of_element_located(self.errorMsg_from_loginArea))
        return self.get_text(self.get_errorMsg_from_loginArea(), doc)
        # return self.driver.find_element(*self.errorMsg_from_loginArea).text

    # 获取错误信息-页面正中间
    def get_errorMsg_from_pageCenter(self):
        doc = "登录页面_获取页面正中间错误信息"
        self.wait_eleVisible(loc.pageCenter_error_info, poll_frequency=0.2, doc=doc)
        return self.get_text(loc.pageCenter_error_info, doc)

    # 忘记密码