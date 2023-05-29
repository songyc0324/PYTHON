# 021
# letters = "python"
# print(letters[0], letters[2])


# 022
# license_plate = "24가 2210"
# print(license_plate[4 : ])


# 023
# string = "홀짝홀짝홀짝"
# print(string[0 : : 2])


# 024
# string = "PYTHON"
# print(string[ : : -1])


# 025
# phone_number = "010-1111-2222"
# new = phone_number.replace('-', ' ')
# print(new)
# 026
# renew = new.replace(' ', '')
# print(renew)


# 027
# url = "http://sharebook.kr"
# url_split = url.split('.')
# print(url_split[-1])


# 028
# lang = "python"
# lang[0] = 'P'
# print(lang)


# 029
# string = 'abcdfe2a354a32a'
# stringA = string.replace('a', 'A')
# print(stringA)


# 030
# string = "abcd"
# string.replace('b', 'B')
# print(string)


# 031
# a = "3"
# b = "4"
# print(a + b)


# 032
# print("Hi" * 3)


# 033
# print('-' * 80)


# 034
# t1 = "python"
# t2 = "java"
# t3 = t1 + ' ' + t2 + ' '
# print(t3 * 4)


# 035
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름 : %s 나이 : %d\n이름 : %s 나이 : %d" % (name1, age1, name2, age2))


# 036
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print("이름 : {} 나이 : {}\n이름 : {} 나이 : {}".format(name1, age1, name2, age2))


# 037
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print(f"이름 : {name1} 나이 : {age1}\n이름 : {name2} 나이 : {age2}")


# 038
# 상장주식수 = "5,969,782,550"
# new_stocks = int(상장주식수.replace(',', ''))
# final = int(new_stocks)
# print(final)
# print(type(final))


# 039
# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[0 : 7])


# 040
# data = "    삼성전자    "
# print(data.strip())


# 041
# ticker = "btc_krw"
# ticker_upper = ticker.upper()
# print(ticker_upper)


# 042
# ticker = "BTC_KRW"
# ticker_lower = ticker.lower()
# print(ticker_lower)


# 043
# test = "hello"
# test_upper = test.capitalize()
# print(test_upper)


# 044
# file_name = "Report_xlsx"
# print(file_name.endswith('xlsx'))


# 045
# file_name = "Report.xlsx"
# print(file_name.endswith(("xlsx", "xls")))


# 046
# file_name = "2020_Report.xlsx"
# print(file_name.startswith('2020'))


# 047
# a = "hello world"
# print(a.split())


# 048
# ticker = "btc_krw"
# new = ticker.split('_')
# print(new)


# 049
# date = "2020-05-01"
# new = date.split('-')
# print(new)


# 050
data = "039490      "
print(data.rstrip())