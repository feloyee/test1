import numpy as np
import pandas as pd

# 返回行索引
df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
print(df)
print(df.index)  # 返回行索引

df1 = pd.DataFrame({'one': [1, 2, 3], 'two': [3, 4, 5], 'three': [5, 6, 7]}, index=['a', 'b', 'c'])
print(df1)
print(df1.index)  # 返回行索引

print(df.values)  # 返回值（二维数组）

print(df.columns)  # 返回列索引

print(df1.T)  # 转置


