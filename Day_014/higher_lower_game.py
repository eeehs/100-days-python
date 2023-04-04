from art import logo,vs
from game_data import data
import random




# setting
Game = True
Score = 0
Compare_A = random.choice(data)
Against_B = random.choice(data)


def cal_score():
    if Score !=0 :
        print(f"You're right!! Current score: {Score}")

def compare_AB():
    global Score
    global Game
    a_vs_b = input("Who has more followers? Type 'A' or 'B': ").lower()
    if Compare_A['follower_count'] > Against_B["follower_count"]:
        if a_vs_b == "a":
            Score +=1
        else:
            Game = False
            print(f"Sorry, that's wrong. Final score: {Score} ")
    elif Compare_A['follower_count'] < Against_B["follower_count"]:
        if a_vs_b == "b":
            Score +=1       
        else:
            Game = False
            print(f"Sorry, that's wrong. Final score: {Score} ")


# Main

while Game:
    print(logo)
    cal_score()
    print(f"Compare A: {Compare_A['name']}, {Compare_A['description']}, {Compare_A['country']}.")
    print(vs)
    print(f"Against B: {Against_B['name']}, {Against_B['description']}, {Against_B['country']}.")
    compare_AB()
    Compare_A = Against_B
    Against_B = random.choice(data)
    if Compare_A == Against_B:
        Against_B = random.choice(data)

