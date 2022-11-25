# import py
import random
from art import logo 
from art import vs
from game_data import data

Current_Score = 0

while True:
    Compare_A = random.choice(data)
    Compare_B = random.choice(data)
    # 같은 값이 나올 수 있음을 방지
    if Compare_A == Compare_B:
        Compare_B = random.choice(data)
    print(logo)
    if Current_Score == 0:
        print("")
    else:
        print(f"You're right! Current score: {Current_Score}.")
    print(f"Compare A: {Compare_A['name']}, {Compare_A['description']}, from {Compare_A['country']} ")
    print("")
    print(vs)
    print("")
    print(f"Compare B: {Compare_B['name']}, {Compare_B['description']}, from {Compare_B['country']} ")
    Type_Choice = input("Who has more followers? Type 'A' or 'B: ")
    
    if Compare_A['follower_count'] > Compare_B['follower_count'] and Type_Choice == 'A':
        Current_Score = Current_Score + 1
    elif Compare_A['follower_count'] > Compare_B['follower_count'] and Type_Choice == 'B':
        print(f"Sorry, that's wrong. Final score: {Current_Score}")
        break
    elif Compare_A['follower_count'] < Compare_B['follower_count'] and Type_Choice == 'A':
        print(f"Sorry, that's wrong. Final score: {Current_Score}")
        break
    elif Compare_A['follower_count'] < Compare_B['follower_count'] and Type_Choice == 'B':
        Current_Score = Current_Score + 1