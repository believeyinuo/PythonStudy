# -*- coding:utf-8 -*-
#@Time : 2019-08-13 
#@Author：lqc
#@Email:572948875@qq.com
#File : class_dict.py

#字典 {} 无序
#1、可以存在空字典
#2、字典里面可以包含任何类型的数据  key:value
#3、字典里面value可以包含任何数据类型的数据
#4、字典里面的元素，根据逗号来分隔
a = {"class" : "python11",
     "student" : 119,
     "teacher" : "nv",
     "score":[99, 88.8, 100.5]}

#字典取值：字典[key]
print(a["score"][-1])

#删除 pop(key)
res = a.pop("teacher")
print(res)

#新增 a[新key] = value
a ["name"] = "huhau"
print(a)

