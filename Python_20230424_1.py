# height = input("키를 입력하세요 : ")
# weight = input("몸무게를 입력하세요 : ")

# bmi = (int(weight) / float(height) ** 2)

# bmi_as_int = int(bmi)

# print(bmi_as_int)






age = input("본인의 나이 입력 : ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
week_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(months_remaining)

message = f"당신의 남은 인생은 {days_remaining}일, {week_remaining}주, {months_remaining}개월"

print(message)