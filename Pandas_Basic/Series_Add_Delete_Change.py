import pandas as pd

data = [100, 200, 300, 400, 500]
index = ["월", "화", "수", "목", "금"]
s = pd.Series(data, index)

# Add -------------------------------------------

# s.loc["토"] = 600       # s.loc[인덱스] = 값
# print(s)


# Delete ----------------------------------------

# del_s = s.drop("수")               # drop 함수는 원본은 유지, 값이 삭제된 시리즈 객체를 반환
# print(del_s)
# del_mul_s = s.drop(["월", "금"])   # 리스트로 묶어서 여러 개 삭제도 가능
# print(del_mul_s)


# Change-----------------------------------------

s.iloc[0] = 1000
print(s)
s.loc["금"] = 10000
print(s)