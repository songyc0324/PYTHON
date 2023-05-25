import pandas as pd
import IPython as ip

# Column ------------------------------------------

# data = {
#     "종가" : [157000, 51300, 68800, 140000],
#     "PER" : [39.88, 8.52, 10.03, 228.38],
#     "PBR" : [4.38, 1.45, 0.87, 2.16]
# }
# index = ["NAVER", "삼성전자", "LG전자", "카카오"]

# df = pd.DataFrame(data, index)
# print(df)


# Row(List) ---------------------------------------

# data = [
#     [157000, 39.88, 4.38],
#     [51300, 8.52, 1.45],
#     [68800, 10.03, 0.87],
#     [140000, 228.38, 2.16]
# ]
# index = ["NAVER", "삼성전자", "LG전자", "카카오"]
# columns = ["종가", "PER", "PBR"]

# df = pd.DataFrame(data = data, index = index, columns = columns)
# print(df)


# Row(Dictionary) ---------------------------------

# data = [
#     {"종가" : 157000, "PER" : 39.88, "PBR" : 4.38},
#     {"종가" : 51300, "PER" : 8.52, "PBR" : 1.45},
#     {"종가" : 68800, "PER" : 10.03, "PBR" : 0.87},
#     {"종가" : 140000, "PER" : 228.38, "PBR" : 2.16}
# ]
# index = ["NAVER", "삼성전자", "LG전자", "카카오"]

# df = pd.DataFrame(data = data, index = index)
# print(df)


# Practice_#1 --------------------------------------

# price = {
#     "시가" : [980, 200, 300],
#     "고가" : [990, 300, 500],
#     "저가" : [920, 180, 300],
#     "종가" : [930, 180, 400]
# }
# CryptoCurrency = ["Bitcoin", "Ripple", "Ethereum"]

# table = pd.DataFrame(data = price, index = CryptoCurrency)
# print(table)


# Practice_#2 --------------------------------------

price = [
    [980, 990, 920, 930],
    [200, 300, 180, 180],
    [300, 500, 300, 400]
]
CryptoCurrency = ["Bitcoin", "Ripple", "Ethereum"]
price_type = ["시가", "고가", "저가", "종가"]

table = pd.DataFrame(data = price, index = CryptoCurrency, columns = price_type)
print(table)
