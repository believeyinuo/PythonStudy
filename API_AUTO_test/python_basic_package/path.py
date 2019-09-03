# -*- coding:utf-8 -*-
#@Time : 2019-08-19 
#@Author：lqc
#@Email:572948875@qq.com
#File : path.py

#新建一个目录/新建一个文件夹
import os
os.mkdir("Alisa")
#跨级新建目录  用/符号来代表路径的不同层级，必须确保上面的层级是存在的
os.mkdir("Alisa/vict")
#转义字符
os.mkdir("D:\\test_python")

#删除 文件，一级一级删除
os.rmdir("Alisa/vict")

#路径的获取
path = os.getcwd()#获取当前工作目录 具体到最后一级目录
print("获取到的当前路径是：{0}".format(path))
path_2 = os.path.realpath(__file__)#获取当前文件所在的绝对路径  具体到模块名

#如何拼接路径
new_path = os.getcwd()+"\python1"
new_path_2 = os.path.join(os.getcwd(), "python11")

#判断是文件还是目录
print(os.path.isfile(os.getcwd()))
print(os.path.isdir(os.getcwd()))

#怎么判断文件是否存在
os.path.exists("/Users/LiQingChun/Desktop/API_AUTO_test/python_basic_package/path.py")

#罗列出当前路径多有文件和目录
print(os.listdir(os.getcwd()))

