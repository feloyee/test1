import tushare as ts

ts_data = ts.get_k_data("601318")
print(ts_data)
print(type(ts_data))