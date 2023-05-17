import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
mark_img = [scissors, rock, paper]

def hand(num) :
   mark = " "
   if num == 0 :
      mark = "가위"
   elif num == 1 :
      mark = "바위"
   elif num == 2 :
      mark = "보"
   return mark

my_choice = int(input("가위바위보를 선택하세요(가위 = 0, 바위 = 1, 보 = 2) : "))
if my_choice < 0 or my_choice > 2 :
   print("잘못된 숫자입니다.")
computer_choice = random.randint(0, 2)

print(f"사용자의 선택은 {my_choice}, {hand(my_choice)}입니다.")
print(mark_img[my_choice])
print(f"컴퓨터의 선택은 {computer_choice}, {hand(computer_choice)}입니다.")
print(mark_img[computer_choice])

if my_choice > computer_choice :
   if my_choice == 2 and computer_choice == 0 :
      print("졌습니다.")
   else :
      print("이겼습니다.")

elif my_choice < computer_choice :
   if my_choice == 0 and computer_choice == 2 :
      print("이겼습니다.")
   else :
      print("졌습니다.")

else :
   print("비겼습니다.")