# -*- coding:utf-8 -*-
#@Time : 2019-08-09 
#@Author：lqc
#@Email:572948875@qq.com
#File : class_list.py

#列表 list 符号[]
a = []
#1、可以存在空列表
#2、列表里面可以包含任何数据类型的数据
b = [1, 0.02, 'hello', [1,2,3], True]
#3、列表里面的元素根据都好来切割
print(len(a))
#4、列表里面的元素也是有索引的，索引值从0开始
#5、获取列表里面的单个值：列表【索引值】
print(a[-1])
#6、列表的切片 同字符串的操作  列表名【索引头：索引尾：步长】
print(a[::2])

#如何往列表里面增加数据
#append  追加  追加在末尾 每次只能添加一个
a.append("秦天")
print("a列表的值{0}".format(a))

#insert 插入数据，指定位置-指定元素的索引值
a.insert(2, "monica")

#pop() 删除,
a.pop()#默认删除最后一个元素
a.pop(2)#传入索引值，就会删除指定位置的索引值
res = a.pop()#pop函数会返回被删除的那个元素
a.remove(1)#指定删除某个值
print()

#修改 a[] = 新值
a[2] = "初心"
