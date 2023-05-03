height = input("키를 입력하세요(m) : ")
weight = input("몸무게를 입력하세요(kg) : ")

bmi = int(weight) / float(height) ** 2
bmi = round(bmi, 2)

if bmi <= 18.5 :
   print("저체중입니다.")
elif bmi <= 22.9 :
   print("정상체중입니다.")
elif bmi <= 24.9 :
   print("과체중입니다.")
else :
   print("비만입니다.")