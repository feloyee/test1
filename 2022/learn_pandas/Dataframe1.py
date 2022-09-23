import numpy as np
import pandas as pd

# DataFrame是一个表格型数据结构，含有一组有序的列
# 可以看成是由Series组成的字典，并且公用一个索引

df = pd.DataFrame({"one": [1, 2, 3], "two": [4, 5, 6], "three": [7, 8, 9]})
print(df)
