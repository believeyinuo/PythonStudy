# -*- coding: utf-8 -*-
# @Time : 2019-08-22 16:24
# @Author : szdl
# @Email : believeyinuo@163.com
# @File : reflection.py
# @Project : API_AUTO_test

# 反射


class GetData:
    Cookie = None


if __name__ == "__main__":
    print(GetData.Cookie)
    setattr(GetData, "Cookie", "小黄")  # 可以直接把类里面的属性值做修改
    hasattr(GetData, "Cookie")  # 判断有没有这个属性
    print(getattr(GetData, "Cookie"))  # attribute 属性
    delattr(GetData, "Cookie")  # 把属性删掉
