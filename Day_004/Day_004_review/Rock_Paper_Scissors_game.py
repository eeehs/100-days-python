rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
#######################################
import random

RPS_list = [rock, paper, scissors]

while True:
    My_Choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if My_Choice not in [0,1,2]:
        print("보기에 없는 숫자입니다. 다시 선택해주세요")
    else:
        break
    
Computer_Choice = random.choice(RPS_list)

print(f"""
MY Chose:

{RPS_list[My_Choice]}

Computer Chose:

{Computer_Choice}
""")
if RPS_list[My_Choice] == Computer_Choice:
    print("draw")
elif RPS_list[My_Choice] == rock and Computer_Choice == scissors:
    print("You win")
elif RPS_list[My_Choice] == paper and Computer_Choice == rock:
    print("You win")
elif RPS_list[My_Choice] == scissors and Computer_Choice == paper:
    print("You win")
else:
    print("You lose")