import random

def generate_numbers() :
    numbers = []
    while len(numbers) < 6 :
        num = random.randint(1, 45)
        if num not in numbers :
            numbers.append(num)
    numbers.sort()
    return numbers

def print_numbers(numbers) :
    for number in numbers :
        print(number, end = ' ')
    print()


print("로또 번호 생성 결과 :", end = ' ')
lotto_numbers = generate_numbers()
print_numbers(lotto_numbers)
