# 롤러코스터 탑승 가능 여부 판독기(조건 : 120cm 이상)

height = float(input("키를 입력하세요(cm) : "))

if height >= 120.0 :
   print("탑승 가능합니다.")
   age = int(input("나이를 입력하세요 : "))

   if age < 12 :
      bill = 0
      print(f"{bill}원입니다.")
   elif age <= 18 :
      bill = 7000
      print(f"{bill}원입니다.")
   elif age >= 65 and age <= 70 :
      bill = 3000
      print(f"경로우대 할인 적용되어 {bill}원입니다.")
   else :
      bill = 12000
      print(f"{bill}원입니다.")

   photo_price = input("사진 촬영을 원하시나요?(yes/no) : ")
   if photo_price == "yes" :
      bill += 1000
      print(f"총 금액 : {bill}원")
   if photo_price == "no" :
      print(f"총 금액 : {bill}원")

else :
   print("탑승 불가능합니다.")