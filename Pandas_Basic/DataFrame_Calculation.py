import pandas as pd
import pyupbit

# Brodcasting -------------------------------------

# df = pyupbit.get_ohlcv("KRW-DOGE")
# df2 = df["open"] + 100
# print(df2)


# Filtering ---------------------------------------

# df = pyupbit.get_ohlcv("KRW-XRP")
# cond = df["close"] > df["open"]
# print(cond)
# print(df[cond])


# ColumnShift -------------------------------------

df = pyupbit.get_ohlcv("KRW-ETH")
# print(df)
df.drop(["volume", "value"], axis = 1, inplace = True)
# print(df)
df["close_shift1"] = df["close"].shift(1)
# print(df)
df["close_change"] = df["close"] - df["close_shift1"]
cond = df["close"] - df["close_shift1"] > 100000
print(df[cond])