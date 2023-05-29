# 101
# "Boolean"


# 102
# print(3 == 5)   # False


# 103
# print(3 < 5)    # True


# 104
# x = 4
# print(1 < x < 5)    # True


# 105
# print((3 == 3) and (4 != 3))    # True


# 106
# print(3 => 4)   # 항상 부등호 먼저


# 107
# if 4 < 3 :
#     print("Hello world")


# 108
# if 4 < 3 :
#     print("Hello world.")
# else :
#     print("Hi, there.")


# 109
# if True :
#     print("1")
#     print("2")
# else :
#     print("3")
# print("4")


# 110
# if True :
#     if False :
#         print("1")
#         print("2")
#     else :
#         print("3")
# else :
#     print("4")
# print("5")


# 111
# test = input("문장을 입력하세요 : ")
# if True :
#     print(test + test)


# 112
# test = input("숫자를 입력하세요 : ")
# test_new = int(test)
# print(test_new + 10)


# 113
# num = input("숫자를 입력하세요 : ")

# if int(num) % 2 == 0 :
#     print("짝수입니다.")
# else :
#     print("홀수입니다.")


# 114
# num = input("숫자를 입력하세요 : ")

# if int(num) + 20 > 255 :
#     print(255)
# else : 
#     print(int(num) + 20)


# 115
# num = input("숫자를 입력하세요 : ")
# num = int(num) - 20

# if num > 255 :
#     print(255)
# elif num < 0 :
#     print(0)
# else :
#     print(num)


# 116
# time = input("시간을 00:00 형식으로 입력하세요 : ")

# if time.endswith("00") :
#     print("정각입니다.")
# else :
#     print("정각이 아닙니다.")


# 117
# fruit = ["사과", "포도", "홍시"]
# word = input("단어를 입력하세요 : ")

# if word in fruit :
#     print("정답입니다.")
# else :
#     print("오답입니다.")


# 118
# warn_investment_list = ["MICROSOFT", "GOOGLE", "NAVER", "KAKAO", "SAMSUNG", "LG"]
# company = input("투자 종목명을 입력하세요 : ").upper()

# if company in warn_investment_list :
#     print("투자 경고 종목입니다.")
# else :
#     print("투자 경고 종목이 아닙니다.")


# 119
# fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
# input_key = input("좋아하는 계절은 : ")

# if input_key in fruit :
#     print("정답입니다.")
# else :
#     print("오답입니다.")
# 120
# input_value = input("좋아하는 과일 : ")

# if input_value in fruit.values() :
    # print("정답입니다.")
# else :
    # print("오답입니다.")


# 121
# data = input("영문자 한 개를 입력하세요 : ")

# if data.islower() :
#     print(data.upper())
# else :
#     print(data.lower())


# 122
# score = input("점수를 입력하세요 : ")
# score = int(score)

# if score > 80 :
#     print("grade is A")
# elif score > 60 and score <= 80 :
#     print("grade is B")
# elif score > 40 and score <= 60 :
#     print("grade is C")
# elif score > 20 and score <= 40 :
#     print("grade is D")
# else :
#     print("score is E")


# 123
# data = input("화폐 금액을 입력하세요 : ")
# data_list = data.split(' ')

# if data_list[-1] == "달러" :
#     print(float(data_list[0]) * 1167, "원")
# elif data_list[-1] == "엔" :
#     print(float(data_list[0]) * 1.096, "원")
# elif data_list[-1] == "유로" :
#     print(float(data_list[0]) * 1268, "원")
# elif data_list[-1] == "위안" :
#     print(float(data_list[0]) * 171, "원")


# 124
# num1 = int(input("첫 번째 숫자 입력 : "))
# num2 = int(input("두 번째 숫자 입력 : "))
# num3 = int(input("세 번째 숫자 입력 : "))
# temp = num1

# if num2 > temp :
#     temp = num2

# if num3 > temp :
#     temp = num3

# print(temp)


# 125
# num = input("휴대전화 번호 입력 : ")

# if num.startswith("011") :
#     print("당신은 SKT 사용자입니다.")
# elif num.startswith("016") :
#     print("당신은 KT 사용자입니다.")
# elif num.startswith("019") :
#     print("당신은 LG유플러스 사용자입니다.")
# else :
#     print("알 수 없습니다.")


# 126
# num = input("우편번호 입력 : ")
# num = str(num[0 : 3])

# gang_list = ["010", "011", "012"]
# do_list = ["013", "014", "015"]
# no_list = ["016", "017", "018", "019"]

# if num in gang_list :
#     print("강북구")
# elif num in do_list :
#     print("도봉구")
# elif num in no_list :
#     print("노원구")


# 127
# license_num = input("주민등록번호 입력 : ")
# license_data = license_num.split('-')[1][0]

# if license_data in ['1', '3'] :
#     print("남자")
# else :
#     print("여자")


# 128
# license_num = input("주민등록번호 입력 : ")
# license_data = license_num.split('-')[1][1 : 3]

# if license_data in ["00", "01", "02", "03", "04", "05", "06", "07", "08"] :
#     print("서울입니다.")
# else :
#     print("서울이 아닙니다.")


# 129
# num = input("주민등록번호 입력 : ")
# stage1 = (int(num[0]) * 2) + (int(num[1]) * 3) + (int(num[2]) * 4) + (int(num[3]) * 5) + (int(num[4]) * 6) + (int(num[5]) * 7)
# stage2 = (int(num[7]) * 8) + (int(num[8]) * 9) + (int(num[9]) * 2) + (int(num[10]) * 3) + (int(num[11]) * 4) + (int(num[12]) * 5)
# stage3 = 11 - ((stage1 + stage2) % 11)

# if stage3 == int(num[-1]) :
#     print("유효한 주민등록번호입니다.")
# else :
#     print("유효하지 않은 주민등록번호입니다.")

# 130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

if float(btc["opening_price"]) + (float(btc["max_price"]) - float(btc["min_price"])) > float(btc["max_price"]) :
    print("상승장입니다.")