import pandas as pd

import pyupbit
df = pyupbit.get_ohlcv("KRW-BTC")

# Column ------------------------------------------

# df["range"] = df["high"] - df["low"]
# print(df)
# print(df["range"])

# df = df.drop("volume", axis = 1)
# print(df)


# Row ---------------------------------------------

new_df = df.drop(["volume", "value"], axis = 1)
date = "2022-10-05 09:00:00"
index = pd.to_datetime(date)
new_df.loc[index] = [100, 110, 120, 130]
# print(new_df)

# print(new_df.tail())
# print(new_df.index[-1])
new_df.drop(new_df.index[-1], axis = 0, inplace = True)
print(new_df)

# StrToTimeData -----------------------------------

# date = ["2021-04-09", "2022-07-11"]
# index = pd.to_datetime(date)
# print(type(date))
# print(type(index))