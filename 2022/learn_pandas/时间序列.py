import numpy as np
import pandas as pd

dt = pd.date_range('2002-01-01', '2002-01-10')  # 自动生成一个时间区间
print("dt = ", dt)

sr = pd.Series(np.arange(100), index=pd.date_range("2020-01-01", periods=100))  # 创建一个Series,以时间序列为索引
print("sr = ", sr)
print(sr.index)  # 查看索引，可以看到是DatetimeIndex
print(sr['2020-02'])  # 查看索引为2月的数据

sr1 = pd.Series(np.arange(1000), index=pd.date_range("2020-01-01", periods=1000))  # 创建一个Series,以时间序列为索引
print(sr1['2021':'2022'])  # 按年切片
print(sr1['2020-05-01':'2021-02-05'])  # 按具体日期切片

print(sr1.resample('W').sum())  # 按周采样，求和
print(sr1.resample('M').sum())  # 按月采样，求和
print(sr1.resample('M').mean())  # 按月采样，求平均值

print(sr1.truncate(before='2021-05-01'))  # 切片，取特定日期之后的数据
print(sr1.truncate(after='2021-05-01'))  # 切片，取特定日期之前的数据
