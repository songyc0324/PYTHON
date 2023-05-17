import random

def generate_numbers() :
    numbers = []
    while len(numbers) < 6 :
        num = random.randint(1, 45)
        if num not in numbers :
            numbers.append(num)
    return numbers

def print_numbers(numbers) :
    for number in numbers :
        print(number, end = ' ')
    print()


print("이번주의 로또 번호는 다음과 같습니다. : ")
lotto_numbers = generate_numbers()
print_numbers(lotto_numbers)