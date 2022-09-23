import pandas as pd
import akshare as ak
import warnings

warnings.filterwarnings("ignore")

# 设置输出显示格式
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.expand_frame_repr", False)
pd.set_option("display.unicode.ambiguous_as_wide", True)
pd.set_option("display.unicode.east_asian_width", True)

# 利用网易财经获取个股历史数据
# 股票代码必须带有证交所字母符号
df = ak.stock_zh_a_hist_163(symbol="sz300024")

print(df.head())

# 利用东财数据接口获取哦所有股票实时数据
# df = ak.stock_zh_a_spot_em()
#
# print(df.head())