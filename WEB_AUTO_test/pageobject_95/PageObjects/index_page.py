# -*- coding:utf-8 -*-
# @Time : 2019-09-14 18:40
# @Author：lqc
# @Email:572948875@qq.com
# File : index_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
from WEB_AUTO_test.pageobject_95.PageLocators.index_page_locators import IndexPageLocators as loc
from WEB_AUTO_test.pageobject_95.Common.basepage import BasePage


class IndexPage(BasePage):

    def isExist_Logout_ele(self):
        # 等待10秒， 元素有没有出现
        # 如果存在就返回True，如果不存在就返回False
        doc = "首页_退出按钮"
        return self.is_eleExist(loc.user_link, doc=doc)
        # try:
        #     WebDriverWait(self.driver, 10).until(
        #         EC.visibility_of_element_located((By.XPATH, '//a[@href="/Index/logout.html"]')))
        #     return True
        # except:
        #     return False

    # 选标操作 - 默认第一个 = 元素定位的时候，过滤掉不可以投的标
    def click_first_bid(self):
        doc = "首页_点击第一个抢投标按钮"
        self.wait_eleVisible(loc.bid_button, doc=doc)
        self.click_element(loc.bid_button, doc)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.bid_button))
        # self.driver.find_element(*loc.bid_button).click()

    # 随机选一个标
    def click_bid_random(self):
        doc = "首页_随机点击抢投标按钮"
        self.wait_eleVisible(loc.bid_button, doc=doc)
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc.bid_button))
        # 找到所有符合的标
        eles = self.get_elements(loc.bid_button, doc)
        # eles = self.driver.find_elements(*loc.bind_button)
        # 随机数
        index = random.randint(0, len(eles)-1)
        eles[index].click()