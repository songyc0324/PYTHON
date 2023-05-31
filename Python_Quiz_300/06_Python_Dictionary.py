# 081
# 082
# 083
# 084
# temp = {}
# print(type(temp))


# 085
# icecream = {"메로나" : 1000, "폴라포" : 1200, "빵빠레" : 1800}
# print(icecream)
# 086
# icecream["죠스바"] = 1200
# icecream["월드콘"] = 1500
# print(icecream)


# 087
ice = {'메로나': 1000,
       '폴로포': 1200,
       '빵빠레': 1800,
       '죠스바': 1200,
       '월드콘': 1500}
# print("메로나 가격 :", ice["메로나"])
# 088
# ice["메로나"] = 1300
# print(ice)
# 089
# del ice["메로나"]
# print(ice)


# 090
# icecream = {"폴라포" : 1200, "빵빠레" : 1800, "월드콘" : 1500, "메로나" : 1000}
# print(icecream["누가바"])


# 091
# inventory = {"메로나" : [300, 20], "비비빅" : [400, 3], "죠스바" : [250, 100]}
# print(inventory)
# 092
# print(inventory["메로나"][0], "원")
# 093
# print(inventory["메로나"][1], "개")
# 094
# inventory["월드콘"] = [500, 7]
# print(inventory)


# 095
# icecream = {"탱크보이" : 1200, "폴라포" : 1200, "빵빠레" : 1800, "월드콘" : 1500, "메로나" : 1000}
# icecream_key = list(icecream.keys())
# print(icecream_key)
# 096
# icecream_value = list(icecream.values())
# print(icecream_value)
# 097
# icecream_price_all = sum(icecream.values())
# print(icecream_price_all)
# 098
# new_product = {"팥빙수" : 2700, "아맛나" : 1000}
# icecream.update(new_product)
# print(icecream)


# 099
# keys = ("apple", "pear", "peach")
# vals = (300, 250, 400)
# result = dict(zip(keys, vals))
# print(result)


# 100
date = ["09/05", "09/06", "09/07", "09/08", "09/09"]
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)