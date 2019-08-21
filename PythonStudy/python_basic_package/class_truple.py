# -*- coding:utf-8 -*-
#@Time : 2019-08-13 
#@Author：lqc
#@Email:572948875@qq.com
#File : class_truple.py

#元祖 tuple 符号()
a = ()
print(type(a))
#1、可以存在空元组
#2、元组里面可以包含任何类型的数据
#3、元组里面的元素，根据逗号来进行分隔
#4、元组里面的元素，也是有索引，索引值从0开始
#5、获取元组里面的元素值：元组[索引值]
#6、元组的切片 元组名[索引头：索引尾：步长]
print(a[0:6:2])

#操作数据库看的时候  会放条件
#元组不支持任何修改（增删改） 'truple' object does not supprot item assignment
a = (1, 0.02, 'hello', [1,2,3], True, (4,5,6), "小小")
#a[3][-1] = "花花"
#a[3].pop()
#print(a[3][1])

b = [1, 0.02, 'hello', [1,2,3], True, (4,5,6), "小小"]
#元组是保护强的数据结构，元组内部元素不能动

#元组只有一个元素，要加一个逗号
c = (1)#int
e = (1,)#truple
d = ("hello")#str
f = ("hello",)#truple
g = ([1,2,3])#list
h = ([1,2,3],)#truple