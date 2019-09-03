# -*- coding:utf-8 -*-
#@Time : 2019-08-19 
#@Author：lqc
#@Email:572948875@qq.com
#File : function.py

#if __name__ == '__main__':#主程序的执行入口，只有在当前模块执行时候才会执行

a = 1
def add(b):
    global a#声明这是一个全局变量
    # a = 5
    print(a+b)
add(10)


# num = input("请输入4位数：")#input是从控制台获取数据，都是字符串形式
# for item in num:
#     print(item)
#     print(int(item) + 5)
#     print("每一位加5然后模10", (int(item) + 5)%10)
#     new_num+=(int(item) + 5)%10

for i in range(1,6):
    print ("*"*i)

# 怎么引入不同的库
#a:在线安装。打开cmd
#1)pip install 模块名
#2)使用国内源去进行安装 pip install 国内源地址 模块名
#3)file-setting-project interpreter

#b:离线安装
#自己去python的官网或者是网上找到离线安装包
#1、解压
#2、拷贝解压后的文件到python安装路径
#3、在cmd里面利用cd一级一级的进入到安装包文件路径  安装文件  setup.py
#python setup.py install

#lib  lib--sitepackage

#1、自己写的，怎么导入
#2、Python自带的，后面安装的第三方库，怎么应用
#1）import 2)from ... import
import email.mine.base
# from email.mime import py

#冒泡排序
a = [1, 7, 4, 89, 34, 2]
# 相邻的两个元素依次比较，一般最多比较n-1趟
for i in range(0, len(a) - 1):
    for j in range(0 , len(a)-1):
        if a[j] > a[j + 1]:
            a[j], a[j +1] = a[j + 1], a[j]


def make_sandwich(a, b, c):
    print ("您的三明治包含了{0}、{1}、{2}".format(a, b, c));

def make_sanwich(*args):
    for item in args:
        all += item
        all += "、"
    print(args)

#关键字参数 key-value **kwags key word
def kw_function(**kwargs):
    print (kwargs)

kw_function(x=1, y=2)

def add_all_num(*L):
    sum = 0
    for item in L:
        sum += item
    print ("和为", sum)