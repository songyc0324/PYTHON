import pandas as pd

data = [
    [157000, 39.88, 4.38],
    [51300, 8.52, 1.45],
    [68800, 10.03, 0.87],
    [140000, 228.38, 2.16]
]
index = ["NAVER", "삼성전자", "LG전자", "카카오"]
columns = ["종가", "PER", "PBR"]

df = pd.DataFrame(data = data, index = index, columns = columns)
# print(df)

# Column ------------------------------------------

# print(df["종가"])       # DataFrame에서 1차원은 Series 형태로 표현
# print(df["PER"])        # DataFrame에서 2차원은 DataFrame 형태로 표현
# print(type(df[["종가", "PBR"]]))


# Row ---------------------------------------------

# print(df.iloc[1 : 3])
# print(df.loc["삼성전자"])
print(df.iloc[[0, 2]])
print(df.loc[["카카오", "삼성전자"]])
print(df.iloc[1 : 4])