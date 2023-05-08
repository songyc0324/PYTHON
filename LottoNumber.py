import random

lotto_number = random.sample(range(1, 46), 6)
lotto_number.sort()

print(f"로또 번호 : {lotto_number} ")