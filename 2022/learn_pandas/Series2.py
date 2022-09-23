import numpy as np
import pandas as pd

sr1 = pd.Series({"a": 1, "b": 2, "c": 3, "d": 4})
sr2 = pd.Series({"a": 10, "c": 30, "d": 40})
sr = sr1 + sr2
print(sr)

# 缺失数据处理
print(sr.isnull())  # 判断缺失数据
print(sr.notnull())  # 判断非缺失数据
print(sr[sr.notnull()])  # 取出非空值
print(sr.dropna())  # 取出非空值

sr3 = sr.fillna(0)  # 填充空值
print(sr3)

sr4 = sr.fillna(sr.mean())  # 填充平均值
print(sr4)
