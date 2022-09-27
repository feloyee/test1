import numpy as np
import pandas as pd

file = pd.read_csv('test.csv')  # 读入csv文件
print(file)
print(type(file))  # 数据格式为DataFrame

file1 = pd.read_csv('test.csv', index_col=0)  # 指定第0列作为索引
print(file1)
file1 = pd.read_csv('test.csv', index_col='date')  # 指定date列作为索引
print(file1)
print(type(file1.index[0]))  # 如果直接以导入的日期作为索引，会发现数据类型为string
file1 = pd.read_csv('test.csv', index_col='date', parse_dates=True)  # 指定date列作为索引，将所有日期(str)数据都转为datetime格式
file1 = pd.read_csv('test.csv', index_col='date', parse_dates=['date'])  # 指定date列作为索引，仅将date列转为datetime格式
print(file1)

# 如果导入的数据没有列名
file2 = pd.read_csv('test1.csv', header=None)  # 如果没有列名，会自动以0、1、2为列名
print(file2)
file2 = pd.read_csv('test1.csv', header=None, names=['a', 'b', 'c'])  # 如果没有列名，以指定的列表为列名
print(file2)
file2 = pd.read_csv('test1.csv', header=None, names=['a', 'b', 'c'], na_values='none')  # 将none字符串解释为NaN缺失值
print(file2)

file3 = pd.read_excel('student.xls')  # 读取excel文件  （需要导入xlrd包）
print(file3)
