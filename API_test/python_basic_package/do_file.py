# -*- coding:utf-8 -*-
#@Time : 2019-08-19 
#@Author：lqc
#@Email:572948875@qq.com
#File : do_file.py

#file txt xml html

file = open("python11.txt", "r+", encoding='gbk')
res = file.read()#读取完一次读取操作后，光标就到文末
print(res)
#r w a
#r+ w+ a+
#rb rb+ wb wb+ ab ab+
#file文件open之后，默认是是r 只读模式
#r+可读可写 先写的话，从头开始覆盖写  读光标之后的内容
#w只写
#w+ 可读可写 如果文件存在，直接清空再重写，如果文件不存在，则新建一个文件
#a 追加 a+ 如果文件存在，则直接追加写在后面，如果不存在，则新建一个文件进行结果写入

#file.readline()按行读取
#file.readlines()读取多行，返回列表

