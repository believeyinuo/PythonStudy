# -*- coding:utf-8 -*-
#@Time : 2019-08-19 
#@Author：lqc
#@Email:572948875@qq.com
#File : error.py

import os
try:
    os.mkdir("Alisa")
except Exception as e:
    print("文件已存在");
    print("错误为:{0}".format(e))
    file = open("error.txt", 'a+')
    file.write(e)
    file.close()
else:#跟try下面的代码一起的，你好我就好
# finally:
    print("我就是这么厉害！！！啦啦啦啦")