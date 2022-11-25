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

#Write your code below this line 👇
import random

my_choice_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

Choice = [rock,paper,scissors]

Computer_choice = random.choice(Choice)
my_choice = Choice[my_choice_number]


print("You chose")
print(my_choice)
print("Computer chose")
print(Computer_choice)

if my_choice == Computer_choice:
    print("draw")
elif my_choice == rock and Computer_choice == scissors:
    print("you win")
elif my_choice == paper and Computer_choice == rock:
    print("you win")
elif my_choice == scissors and Computer_choice == paper:
    print("you win")
else:
    print("you lose")