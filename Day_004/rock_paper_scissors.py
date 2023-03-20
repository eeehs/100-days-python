import random

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

rock_paper_scissors =[rock,paper,scissors]
computer_choice = random.choice(rock_paper_scissors)
my_choice = rock_paper_scissors[int(input("what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))] 

print(my_choice)
print("Computer chose: \n")
print(computer_choice)

if my_choice == computer_choice:
    print("Draw!!")
elif my_choice == rock and computer_choice == paper:
    print("You lose")
elif my_choice == paper and computer_choice == scissors:
    print("You lose")
elif my_choice == scissors and computer_choice == rock:
    print("You lose")
else:
    print("You win!!")