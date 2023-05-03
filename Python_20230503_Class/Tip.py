# 팁 계산기
# 총 주문 금액
# 팁의 비율(%)
# 팁 포함 총 지불 금액
# 몇 명이서 지불할 것인가
# 인당 지불 금액 

print("팁 계산기")

order = float(input("총 얼마를 주문했는가?($) "))
tip = int(input("팁을 얼마나 내야 하는가?(%) "))
people = int(input("몇 명이서 나눠 내야 하는가? "))

tip_as_percent = tip / 100
total_tip = order * tip_as_percent
total_bill = order + total_tip
bill_per_person = total_bill / people

final_bill = round(bill_per_person, 2)
print(f"팁 포함해서 인당 지불해야 할 금액은 {final_bill}$")