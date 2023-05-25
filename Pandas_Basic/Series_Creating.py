import pandas as pd

# arr = [0, 1, 2, 3]
# data = [100, 200, 300]
# index = ['월', '화', '수']

# # s = pd.Series(arr)
# # print(s)

# ss = pd.Series(data, index)
# print(ss)

# print(ss.index)
# print(ss.values)

# -------------------------------------------------


icecream = ["메로나", "누가바", "빠삐코"]
price = [500, 800, 200]

table = pd.Series(price, icecream)

print(table)

# -------------------------------------------------