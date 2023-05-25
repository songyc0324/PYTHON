import pandas as pd

data = [
    ["3R", 1510, 7.36],
    ["3SOFT", 1790, 1.65],
    ["ACTS", 1185, 1.28]
]
index = ["037730", "036360", "005760"]
columns = ["종목명", "현재가", "등락률"]

df = pd.DataFrame(data = data, index = index, columns = columns)
# print(df)

# Part_Value --------------------------------------

print(df.iloc[2, 0])
print(df.iloc[1, 1])
print(df.loc["037730", "등락률"])