# print("오늘은 파이썬 디버깅을 연습하고 있습니다")

# print('디버깅 "+" 연습중입니다')

# print('오늘은(“수요일" + "입니다")')

# print("내일은 목요일 입니다")

# print("나는" + input("당신의 이름은 무엇입니까? ") + "입니다")

# print(len(input("당신의 이름은 무엇입니까?")))

'''
name = input("당신의 이름은 무엇입니까? ")
length = len(name)
print(length)
'''

'''
a = input("a값 입력 : ")
b = input("b값 입력 : ")

c = a
a = b
b = c

print("a : " + a)
print("b : " + b)
'''

'''
movie = input("좋아하는 영화 입력 : ")
movie_char = input("주인공 입력 : ")

print("내가 좋아하는 영화는 " + movie + "(이)고, 주인공은 " + movie_char + "(이)다.")
'''

# print("Hello"[0])

number = input("두 자리 숫자 입력 : ")
first = int(number[0])
second = int(number[1])
print(first + second)
