import numpy as np
import pandas as pd
import datetime

# python的常规时间处理方法
dt = datetime.datetime.strptime('2010-01-01', '%Y-%m-%d')  # 把字符串转为时间对象
print("dt = ", dt)
print(type(dt))

import dateutil

dt1 = dateutil.parser.parse('2001-01-01')  # 利用dateutil库中的parser方法，可以对多种日期字符串进行自动解析
dt2 = dateutil.parser.parse('2001/01/01')
print("dt1 = ", dt1)
print(type(dt1))
print("dt2 = ", dt2)
print(type(dt2))

# pandas库中的批量时间处理方法
dt3 = pd.to_datetime(['2002-01-01', '2002-01-02', '2002-01-03', '2002/01/04', '2002/jan/05'])
# to_datetime()方法会自动解析各种格式的日期字符串
print("dt3 = ", dt3)
print(type(dt3))

