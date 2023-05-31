# 131
# fruit = ["apple", "orange", "watermelon"]
# for i in fruit :
    # print(i)
# 132
# for i in fruit :
#     print("#####")


# 133
# print("A")
# print("B")
# print("C")


# 134
# print("출력 :", "A")
# print("출력 :", "B")
# print("출력 :", "C")


# 135
# data = 'A'
# print(data.lower())
# data = 'B'
# print(data.lower())
# data = 'C'
# print(data.lower())


# 136
# for i in [10, 20, 30] :
#     print(i)


# 137
# for i in [10, 20, 30] :
#     print(i)


# 138
# for i in [10, 20, 30] :
#     print(i)
#     print("-------")


# 139
# print("++++")
# for i in [10, 20, 30] :
#     print(i)


# 140
# for i in [1, 2, 3, 4] :
#     print("-------")


# 141
# sell = [100, 200, 300]
# for i in sell :
#     print(i + 10)


# 142
# menu = ["김밥", "라면", "튀김"]
# for i in menu :
#     print("오늘의 메뉴 : %s" % i)


# 143
# com = ["SK하이닉스", "삼성전자", "LG전자"]
# for i in com :
#     print(len(i))


# 144
animal = ["dog", "cat", "parrot"]
# for i in animal :
#     print("%s %d" % (i, len(i)))
# 145
# for i in animal :
#     print(i[0])


# 146
# num = [1, 2, 3]
# for i in num :
#     print("3 x " + str(i))
# 147
# for i in num :
    # print("3 x %d = %d" % (i, i * 3))


# 148
# letter = ['가', '나', '다', '라']
# for i in letter[1 : ] :
#     print(i)
# 149
# for i in letter[ : : 2] :
#     print(i)
# 150
# for i in letter[ : : -1] :
#     print(i)


# 151
# num = [3, -20, -3, 44]
# for i in num :
#     if i < 0 :
#         print(i)


# 152
# num = [3, 100, 23, 44]
# for i in num :
#     if i % 3 == 0 :
#         print(i)


# 153
# num = [13, 21, 12, 14, 30, 18]
# for i in num :
#     if (i < 20) and (i % 3 == 0) :
#         print(i)


# 154
# string = ["I", "study", "python", "language", "!"]
# for i in string :
#     if len(i) >= 3 :
#         print(i)


# 155
# letter = ['A', 'b', 'c', 'D']
# for i in letter :
#     if i.isupper() :
#         print(i)
#     else :
#         continue
# 156
# for i in letter :
#     if i.islower() :
#         print(i)
#     else :
#         continue


# 157
# animal = ["dog", "cat", "parrot"]
# for i in animal :
#     first = i[0].upper()
#     print(first + i[1 :])


# 158
# file_list = ["hello.py", "ex01.py", "intro.hwp"]
# for i in file_list :
#     new = i.split('.')
#     print(new[0])


# 159
# file_list = ["intra.h", "intra.c", "define.h", "run.py"]
# for i in file_list :
#     if i.endswith(".h") :
#         print(i)
#     else :
        # continue
# 160
# for i in file_list :
#     new = i.split('.')
#     if new[1] == 'h' or new[1] == 'c' :
#         print(i)
#     else :
#         continue


# 171
price_list = [32100, 32150, 32000, 32500]
# for i in range(0, 4) :
#     print(price_list[i])
# 172
# for i, data in enumerate(price_list) :
#     print(i, data)
# 173
# for i in range(0, 4) :
#     print(len(price_list) - 1 - i, price_list[i])
# 174
# for i in range(1, 4) :
#     print(90 + (10 * i), price_list[i])


# 175
# my_list = ['가', '나', '다', '라']
# for i in range(0, 3) :
#     print(my_list[i], my_list[i + 1])


# 176
# my_list = ['가', '나', '다', '라', '마']
# for i in range(len(my_list) - 2) :
#     print(my_list[i], my_list[i + 1], my_list[i + 2])


# 177
# my_list = ['가', '나', '다', '라']
# for i in range(3, 0, -1) :
#     print(my_list[i], my_list[i - 1])

# 178
# my_list = [100, 200, 400, 800]
# for i in range(0, len(my_list) - 1) :
#     print(my_list[i + 1] - my_list[i])


# 179
# my_list = [100, 200, 400, 800, 1000, 1300]
# for i in range(0, 4) :
#     avg = (my_list[i] + my_list[i + 1] + my_list[i + 2]) / 3
#     print(avg)


# 180
# low_prices = [100, 200, 400, 800, 1000]
# high_prices = [150, 300, 430, 880, 1000]
# volatility = []
# for i in range(0, len(low_prices)) :
#     volatility.append(high_prices[i] - low_prices[i])
# print(volatility)


# 181
# apart = [["101호", "102호"],
#          ["201호", "202호"],
#          ["301호", "302호"]]
# print(apart)


# 182
# stock = [["시가", 100, 200, 300],
#          ["종가", 80, 210, 330]]
# print(stock)


# 183
# stock = {"시가" : [100, 200, 300], "종가" : [80, 210, 330]}
# print(type(stock))


# 184
# stock = {"10/10" : [80, 110, 70, 90], "10/11" : [210, 230, 190, 200]}
# print(type(stock))


# 185
# apart = [[101, 102],
#          [201, 202],
#          [301, 302]]
# for row in apart :
#     for col in row :
#         print(col, "호")
# 186
# for i in apart[ : : -1] :
#     for j in i :
#         print(j, "호")
# 187
# for i in apart[ : : -1] :
#     for j in i[ : : -1] :
#         print(j, '호')
# 188
# for i in apart :
#     for j in i :
#         print(j, '호')
#         print("-----")
# 189
# for i in apart :
#     for j in i :
#         print(j, '호')
#     print("-----")
# 190
# for i in apart :
#     for j in i :
#         print(j, '호')
# print("-----")


# 191
# data = [[2000, 3050, 2050, 1980],
#         [7500, 2050, 2050, 1980],
#         [15450, 15050, 15550, 14900]]
# for i in data :
#     for j in i :
#         print(j + (j * 0.00014))
# 192
# for i in data :
#     for j in i :
#         print(j + (j * 0.00014))
#     print("----")
# 193
# result = []
# for i in data :
#     for j in i :
#         result.append(j * 1.00014)
# print(result)
# 194
# result = []
# for i in range(0, 3) :
#     sub = []
#     for j in data[i] :
#         sub.append(j * 1.00014)
#     result.append(sub)
# print(result)


# 195
ohlc = [["open", "high", "low", "close"], 
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
# for i in ohlc[1 : ] :
#     print(i[3])
# 196
# for i in ohlc[1 : ] :
#     if i[3] > 150 :
#         print(i[3])
# 197
# for i in ohlc[1 : ] :
#     if i[3] >= i[0] :
#         print(i[3])
# 198
# volatility = []
# for i in ohlc[1 : ] :
#     volatility.append(i[1] - i[2])
# print(volatiilty)
# 199
# for i in ohlc[1 : ] :
#     if i[3] > i[0] :
#         print(i[1] - i[2])
# 200
profit = 0
for i in ohlc[1 : ] :
    temp = i[3] - i[0]
    profit += temp
print(profit)