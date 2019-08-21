# -*- coding:utf-8 -*-
#@Time : 2019-08-09
#@Author：lqc
#@Email:572948875@qq.com
#File : class_str.py

s = 'hello'
#1:字符串里面元素：单个字母、数字、汉字、单个符号 都称为一个元素
#len(数据)统计数据的长度
#2：字符串取值：字符串名[索引值]
#索引：从0开始标记
#字符串取多个值：切片  字符串名[索引头：索引尾：步长]，步长默认为1
print(s[1:5:1])#取头不取尾
print(s[1:5:2])
print(s[1:5:3])
print(s[:])
print(s[:4])#取到4为止，0-3
print(s[3:])#3以后的全取

#  h  e  l  l  o  !
#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1
#小题目：倒序输出s的值，输出结果为！olleh
print(s[-1:-7:-1])
print(s[::-1])

#字符串的分割  字符串.split(可以指定切割符号) 返回一个列表类型的数据，列表里面的子元素都是字符串类型
#指定的切割符，被切走了
#可以指定切割次数
s = ' hello!'
print(s.split(" ", 1))

#字符串的替换 字符串.replace(指定替换值，新值)
#可以指定替换次数
new = s.replace('o', '@', 1)

#字符串的去除指定字符  字符串.strip(指定字符)
#默认去掉空格
#只能去掉头和尾的指定字符
print(s.strip())

#字符串的拼接  保证+左右两边的变量值类型要一致
s_1 = 'python'
s_2 = '中秋节快乐'
s_3 = 666
print(s_1, s_2)
print(s_1 + s_2)
print(s_1 + s_2 + str(s_3))

#字符串格式化输出  %format
age = 18
name = '小恒星'
score = 99.99
print("paython11期的" + name + "今年" + str(age) + "岁！")
#格式化输出1：format 特点 {}  用这个{}来占坑
print("python11期的{0}, 今年{1}岁！".format(name, age))

#格式化输出2：% %s字符串 %d数字 %f浮点数
print("paython11期的%s, 今年%d岁！考试考了%.1f"%(name, age, score))
#%s 可以填任何数据
#%d 只能填数字  整型  浮点数
#%f 可以填数字