from art import logo , vs
from game_data import data
import random


i = 0
continue_game = True
def compare(choice_A_B):
    """비교 후 값 도출 """
    global i
    global continue_game
    if choice == choice_A_B:
        i = i + 1
    else:
        print("you lose")
        continue_game = False
        return continue_game


def score():
    global i
    if i == 0:
        pass
    else:
        print(f"You're right! Current score: {i}")
    
    

# MAIN GAME
while continue_game:

    compare_A = random.choice(data)
    compare_B = random.choice(data)
    # 같은 값 방지
    if compare_A == compare_B:
        compare_B = random.choice(data)
    # 미리 결과 결정 
    if compare_A['follower_count'] > compare_B['follower_count']:
        choice = "a"
    else:
        choice = "b"
 
    print(logo)
    score()
    print(f"""
    Compare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}
    {vs}
    Against B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']}
    """)
    
    choice_A_B = input("Who has more followers? Type 'A' or 'B': ").lower()

    compare(choice_A_B)



