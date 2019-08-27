# -*- coding:utf-8 -*-
#@Time : 2019-08-27 
#@Author：lqc
#@Email:572948875@qq.com
#File : learn_pandas.py

import pandas as pd

df = pd.read_excel("test_data.xlsx", sheet_name = "rechatge")
print(df.values)
print(df.ix[1])         # 读指定行  二维矩阵
print(df.ix[1].values)  # 读指定行  列表
print(df.ix[1, 1])      # 第一行第一列
print(df.ix[:])  # 读所有的
print(df.ix[:].values)  # 读所有的
print(df.ix[:["url"]].values) # 指定的列
print(df.ix[1, ["url", "data"]].to_dict()) # 指定的列
print(df.index.values)
test_data = []
for i in df.index.values:
    row_data = df.ix[i, ["url", "data"]].todict()
    test_data.append(row_data)
print(test_Data)