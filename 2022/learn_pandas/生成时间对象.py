import numpy as np
import pandas as pd

dt = pd.date_range('2002-01-01', '2002-01-10')  # 自动生成一个时间区间
print("dt = ", dt)
dt1 = pd.date_range('2002-01-01', '2002-02-10', periods=7)  # 自动生成一个时间区间，指定日期间隔，间隔频率默认为day
print("dt1 = ", dt1)
dt2 = pd.date_range('2002-01-01', '2002-01-2', freq="H")  # 自动生成一个时间区间，指定日期间隔，指定间隔频率为hour
print("dt2 = ", dt2)
dt3 = pd.date_range('2002-01-01', periods=6, freq="W")  # 间隔区间为6，指定间隔频率为week，默认起始日期为周日
print("dt3 = ", dt3)
dt4 = pd.date_range('2002-01-01', periods=10, freq="W-MON")  # 间隔区间为10，指定间隔频率为week，默认起始日期为周一
print("dt4 = ", dt4)
dt5 = pd.date_range('2002-01-01', periods=10, freq="B")  # 间隔区间为10，指定间隔为跳过周末（保留工作日）
print("dt5 = ", dt5)
print(dt5[0]) # 输出第一个日期
print(type(dt5[0]))  # 第一个日期的格式为timestamp
print(dt5[0].to_pydatetime())  # 把timestamp转为datetime对象
