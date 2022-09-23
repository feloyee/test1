import numpy as np
import pandas as pd

# Series 一维数据对象
# 类似于一维数组的对象，由一组数据和一组与之相关额数据标签（索引）组成
a1 = pd.Series([2, 3, 4, 5, 6])
print(a1)

a2 = pd.Series([2, 3, 4, 5], index=['a', 'b', 'c', 'd'])  # 创建自定义索引
print(a2)

a3 = pd.Series(np.arange(5))  # 可以导入array数据
print(a3)

print(a2[1])  # 可以同通过下标访问

print(a1 + a3)  # 可以进行计算

print(a1[1:])  # 可以切片

a4 = pd.Series({"a": 1, "b": 2, "c": 3})  # 可以导入字典类型数据
print(a4)

print(a4['c'])  # 可以通过字典key访问value

print("a" in a4)  # 判断key是否包含在数组字典内

for i in a4:
    print(i)

print(a4.index)  # 打印索引
print(a4.values)  # 打印值

print(a4["b":"c"])  # 通过标签切片

