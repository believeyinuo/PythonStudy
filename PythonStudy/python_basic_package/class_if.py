# -*- coding:utf-8 -*-
#@Time : 2019-08-13 
#@Author：lqc
#@Email:572948875@qq.com
#File : class_if.py

#if 控制语句 分支 for while
#判断语句 if...elif...else
#空数据==False 非空元素==True

#input()函数 从控制台获取一个数据 获取的数据是字符串类型
#isdigtal
#age = int(input("请输入你的年龄"))
#if age > 18:
#    print("恭喜你，你成年了！")
#elif 18 > age >= 0:
#    print("小屁孩")
#else:
#    print("输入有误")
"""
total = int(input("请输入购买总金额"))
if total < 50:
    print("不好意思，你没法享受折扣")
    print("您需要支付{0}元".format(total))
elif 50 <= total <= 100:
    print("您将享受10%折扣")
    print("您需要支付{0}元".format(total*(1-0.1)))
elif total > 100:
    print("您将享受20%折扣")
    print("您需要支付{0}元".format(total*(1-0.2)))
  """

import random
num_1 = random.randint(1,9) #两边都包含

