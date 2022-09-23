import numpy as np
import pandas as pd

# DataFrame是一个表格型数据结构，含有一组有序的列
# 可以看成是由Series组成的字典，并且公用一个索引

# 通过字典创建DataFrame
df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
print(df)

df1 = pd.DataFrame({'one': [1, 2, 3], 'two': [3, 4, 5], 'three': [5, 6, 7]}, index=['a', 'b', 'c'])
print(df1)

# 通过Series从创建DataFrames
df2 = pd.DataFrame(
    {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']), 'two': pd.Series([1, 2, 3, 4], index=['b', 'c', 'a', 'd'])})
print(df2)

# 通过导入csv文件创建DataFrame
df3 = pd.read_csv('test.csv')
print(df3)

# 将DataFrame写入csv文件
df.to_csv("test1.csv")

