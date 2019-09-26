# -*- coding:utf-8 -*-
# @Time : 2019-09-15 11:53
# @Author：lqc
# @Email:572948875@qq.com
# File : test_01_invest.py

# 前置条件
######################尽量不要依赖测试环境数据，如果没有，就自己造环境#############
# 1、用户已登录
# 2、有能够投资的标  # 如果没有标，则先加标。  # 接口加标
# 3、用户有余额可以投资
    # 1、1个亿
    # 2、接口方式：查询当前用户还有多少钱，如果小于用例中的投资的金额，那就充值


# 步骤
# 1、在首页选标--不根据标名，根据抢投标。默认第一个标
#    标页面-获取一下投资前的用户余额
# 2、标页面-输入投资金额、点击投资按钮
# 3、标页面-点击投资成功的弹出框-查看并激活，进入个人页面

# 断言
# 钱  投资后的金额，是不是少了投资的量
# 个人页面-获取投资后的金额
# 投资前的金额 - 投资后的金额 = 投资金额
# 投资记录对不对
# 利息对不对

# 异常用例：非常好创造环境，非常好写的。
# 异常用例：全投操作  标的可投金额 > 个人余额
#         投资的金额 > 标的可投金额   # 找到满足这种条件的标、用户

import unittest
import ddt
import logging
from selenium import webdriver
from WEB_AUTO_test.pageobject_95.TestDatas import Common_Datas as CD
from WEB_AUTO_test.pageobject_95.PageObjects.login_page import LoginPage
from WEB_AUTO_test.pageobject_95.PageObjects.index_page import IndexPage
from WEB_AUTO_test.pageobject_95.PageObjects.bid_page import BidPage
from WEB_AUTO_test.pageobject_95.PageObjects.user_page import UserPage
from WEB_AUTO_test.pageobject_95.TestDatas import invest_datas as ID
import time
import pytest


@ddt.ddt
class TestInvest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化浏览器会话
        logging.info("======用例类前置：初始化浏览器会话，登录前程贷系统==========")
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(CD.web_login_url)
        LoginPage(cls.driver).login(CD.user, CD.password)
        # 首页 - 选一个标来投资 - 直接选第一个标 - ---/ 随机选一个
        IndexPage(cls.driver).click_first_bid()
        cls.bid_page = BidPage(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        logging.info("========用例类后置：关闭浏览器会话，清理环境=============")
        cls.driver.quit()

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        logging.info("=======每一个用例后置：刷新当前页面=================")
        self.driver.refresh()
        time.sleep(0.5)

    @pytest.mark.smoke
    def test_invest_1_success(self):
        logging.info("**********投资用例：正常场景-投资成功******")
        # 步骤
        # 1、在首页选标--不根据标名，根据抢投标。默认第一个标
        #    标页面-获取一下投资前的用户余额
        userMoney_beforeInvest = self.bid_page.get_user_money()
        # 2、标页面-输入投资金额、点击投资按钮
        self.bid_page.invest(ID.success["money"])
        # 3、标页面-点击投资成功的弹出框-查看并激活，进入个人页面
        self.bid_page.click_activeButton_on_success_popup()

        # 断言
        # 钱  投资后的金额，是不是少了投资的量
        # 个人页面-获取投资后的金额
        userMoney_afterInvest = UserPage(self.driver).get_user_leftMoney()
        # 投资前的金额 - 投资后的金额 = 投资金额
        assert ID.success["money"] == int(float(userMoney_beforeInvest) - float(userMoney_afterInvest))
        # 投资记录对不对

    @ddt.data(*ID.wrong_format_money)
    def test_invest_0_failed_no100(self, data):
        logging.info("********投资用例：异常场景，投资金额为非100的整数倍，错误的格式等*****")
        # 标页面 - 获取投资前的个人余额
        userMoney_beforeInvest = self.bid_page.get_user_money()
        # 标页面 - 输入投资金额，点击投标按钮
        self.bid_page.invest(data["money"])
        # 获取提示信息
        errorMsg = self.bid_page.get_errorMsg_from_pageCenter()
        # 刷新
        self.driver.refresh()
        # 获取用户余额
        userMoney_afterInvest = self.bid_page.get_user_money()
        # 断言
        assert errorMsg == data["check"]
        assert userMoney_afterInvest == userMoney_beforeInvest

    def test_invest_failed_no10(self):
        pass
