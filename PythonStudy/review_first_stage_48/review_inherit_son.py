# -*- coding:utf-8 -*-
# @Time : 2019-08-26
# @Author：lqc
# @Email:572948875@qq.com
# File : review_inherit_son.py

from PythonStudy.review_first_stage_48.review_inherit_father import HttpRequest


# 继承
# 重写：跟父类的函数名重复
# 拓展：父类里面没有的
class PythonHttpRequest(HttpRequest):
    def __init__(self, a, b, url, data):  # 超继承
        super(PythonHttpRequest, self).__init__(url, data)  # 调用父类里面的__init__方法
        # super(子类名, self).父类跟子类函数同名的方法(参数)
        self.a = a
        self.b = b

    def print_msg(self):
        self.get_request()  # 类里面的方法 属性 只能是实例调用
        print("我是一个没有用的函数，我在这里要调用父类的函数")

    def add(self):
        print("a + b = ", self.a + self.b)

# 继承的时候，子类要不要传初始化参数 看父类
url = 'https://client.xsdsport.com/erasports/client/customer/login'
data = {"mobilephone":"13068712118", "pwd": "123456"}
a = 1
b = 2
PythonHttpRequest(a, b, url, data).print_msg()
PythonHttpRequest(a, b, url, data).get_request()
