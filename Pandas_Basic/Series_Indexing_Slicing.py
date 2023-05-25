import pandas as pd

data = [100, 200, 300, 400, 500, 600, 700]
index = ["월", "화", "수", "목", "금", "토", "일"]
s = pd.Series(data, index)

# Indexing / in range -----------------------------
# print(s)
# print(s.iloc[0])
# print(s.iloc[2])
# print(s.loc["수"])


# Indexing / not range ----------------------------

target = [2, 5]
print(s.iloc[target])
print(s.iloc[[1, 3, 4]])    # 특정 인덱스를 직접 입력하려면 대괄호 안에 대괄호를 하나 더 추가하고 입력
print(s.loc[["화", "토"]])
target_2 = ["월", "수", "일"]
print(s.loc[target_2])

# Slicing -----------------------------------------
# print(s.iloc[0 : 1])
# print(s.iloc[3 : 6])
# print(s.loc["수" : "일"])      # 슬라이싱 loc는 끝 값을 포함