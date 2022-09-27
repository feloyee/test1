import numpy as np
import pandas as pd

df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]}, index=['a', 'b', 'c'])
print(df)
print(df.mean())  # mean()函数，对列求平均值
print(df.mean(axis=1))  # 按行求平均值

print(df.sum())  # sum()方法，默认按列求和
print(df.sum(axis=1))  # sum()方法，修改为按行求和

print(df.sort_values(by='two'))  # sort_values()，方法按值排序，默认升序
print(df.sort_values(by='two', ascending=False))  # sort_values()，方法按值排序，修改为降序排列
print(df.sort_values(by='a', ascending=False, axis=1))  # sort_values()，方法按值排序，修改为降序排列，按行排序

print(df.sort_index())  # sort_index()方法，按索引排序，默认升序
print(df.sort_index(ascending=False))  # sort_index()方法，按索引排序，降序


