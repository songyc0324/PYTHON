import random

name_class = input("아이스크림 내기에 참여할 사람들 이름을 입력, 쉼표를 사용해서 이름을 구분해줘 : ")
names = name_class.split(", ")

num_item = len(names)

random_choice = random.randint(0, num_item - 1)

person_who_pay = names[random_choice]

print(f"{person_who_pay}(이)가 아이스크림 사기!")