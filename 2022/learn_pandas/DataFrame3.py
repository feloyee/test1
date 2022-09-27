import numpy as np
import pandas as pd

df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
df1 = pd.DataFrame({'one': [1, 2, 3], 'two': [3, 4, 5], 'three': [5, 6, 7]}, index=['a', 'b', 'c'])
print(df)
print(df1)

print(df1["one"])  # 返回某一列
print(df1['one']['a'])  # 返回某一个单元格的值，先列后行

# 推荐的获取特定单位数据的方法
print(df1.loc['a', 'one'])  # 指定用标签获取数据，先行后列
print(df1.loc['a'])
print(df1.loc['a', :])  # 显示指定行的值

print(df1.loc[['a', 'c'],])  # 花式索引
print(df1.loc[['a', 'c'], 'three'])

# 数据对齐和缺失数据
df = pd.DataFrame({'two': [1, 2, 3, 4], 'one': [4, 5, 6, 7]}, index=['c', 'd', 'b', 'a'])
print(df)
df3 = df + df1  # 制造空值单元
print(df3.fillna(0))  # 在空值单元内填入0
print(df3.dropna())  # 丢弃有空值数据行
print(df3.dropna(how='all'))  # 只有该行所有记录均为空才不显示
print(df3.dropna(axis=1))  # 列记录里有1个空值就不显示整列
print(df3.dropna(axis=1,how='all'))   # 列记录里全部为空值，则不显示该列

