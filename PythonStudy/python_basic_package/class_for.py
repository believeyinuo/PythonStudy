# -*- coding:utf-8 -*-
#@Time : 2019-08-13 
#@Author：lqc
#@Email:572948875@qq.com
#File : class_for.py

#循环 for while
#for item in 某个数据类型:   #字符串  列表  元组  字典  集合
#for 循环的循环次数 有数据的元素个数决定
s = 'hello'
l = [1,2,3]
d = {"age":18, "name":"减压单"}#字典类型的数据  是遍历访问的key
print(d.values())
print(d.keys())
for item in d:
    print(d[item])

#range函数 rang(头，尾，步长)，头默认为0，步长默认为1，取头不取尾
range(1, 6)
range(1, 6, 2)
print(list(range(1,5,1)))#为了方便观察，转为列表形式
