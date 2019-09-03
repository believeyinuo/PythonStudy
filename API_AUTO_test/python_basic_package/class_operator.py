# -*- coding:utf-8 -*-
#@Time : 2019-08-13 
#@Author：lqc
#@Email:572948875@qq.com
#File : class_operator.py

#运算符 5大类
#算数运算符 + - * / %
#模运算  取余运算
a = 4
print(a % 3)

#赋值运算 = += -=

#比较运算符 > >= < <= != ==
#比较结果返回的值是bool值 True False
print("get".upper() == "GET")
print("get" == "GET".lower())

#逻辑运算符 and or not
#逻辑运算符结果返回值是布尔值 True False
b = 10
c = 5
print(b > 11 and b < 5)

#成员运算符 in not in
#返回值  也是布尔值 True False
s = 'hello'
print('o' not in s)
l = [1,2,3]
print(s in l)
d = {"age":18, "name":"减压单"}
print("18" in d)#false
print("age" in d)#true 字典判断key是否存在
