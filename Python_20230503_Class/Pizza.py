
print("파이썬 피자에 오신 것을 환영합니다!")

size = input("원하는 피자 사이즈를 입력하세요(S / M / L) : ")
if size == "S" :
   tot_price = 15000
   pizza_price = 15000
#   print(f"{price}원입니다.")
if size == "M" :
   tot_price = 20000
   pizza_price = 20000
#   print(f"{price}원입니다.")
if size == "L" :
   tot_price = 30000
   pizza_price = 30000
#   print(f"{price}원입니다.")

option_1 = input("페퍼로니를 추가하시겠습니까?(yes / no) : ")
if option_1 == "yes" :
   tot_price += 2000
   pepperoni_price = 2000
#   print(f"총 금액은 {price}원입니다.")
if option_1 == "no" :
#   print(f"총 금액은 {price}원입니다.")
   tot_price += 0
   pepperoni_price = 0

option_2 = input("치즈를 추가하시겠습니까?(yes / no) : ")
if option_2 == "yes" :
   tot_price += 3000
   cheese_price = 3000
#   print(f"총 금액은 {price}원입니다.")
if option_2 == "no" :
#   print(f"총 금액은 {price}원입니다.")
   tot_price += 0
   cheese_price = 0

print(f"총 지불하실 금액은 피자 {pizza_price}원, 페퍼로니 추가 {pepperoni_price}원, 치즈 추가 {cheese_price}원을 더한 {tot_price}원입니다.")