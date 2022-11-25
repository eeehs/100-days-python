from art import logo
import random

def Welcome():
    print(logo)
    print(f"""
    Welcome to the Number Guessing Game!
    i'm thinking of a number between 1 and 100.
    psset, the correct answer is {real_number}
    """)

def easy_mode():
    easy_mode_number = 10
    while True:
        if easy_mode_number == 0:
            print("you've run out of guesses, you lose")
            break
        print(f"you have {easy_mode_number} attempts remaining to guess ")
        guess = int(input("Make a guess: "))
        if guess < real_number:
            print("Too low.")
            print("Guess again")
            easy_mode_number = easy_mode_number - 1
        elif guess == real_number:
            print(f"You got it! The answer was {real_number}.")
            break
        else:
            print("Too high")
            print("Guess again")
            easy_mode_number = easy_mode_number - 1

def hard_mode():
    hard_mode_number = 5
    while True:
        if hard_mode_number == 0:
            print("you've run out of guesses, you lose")
            break
        print(f"you have {hard_mode_number} attempts remaining to guess ")
        guess = int(input("Make a guess: "))
        if guess < real_number:
            print("Too low.")
            print("Guess again")
            hard_mode_number = hard_mode_number - 1
        elif guess == real_number:
            print(f"You got it! The answer was {real_number}.")
            break
        else:
            print("Too high")
            print("Guess again")
            hard_mode_number = hard_mode_number - 1


real_number = random.randint(1, 100)


Welcome()

Choose_a_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if Choose_a_difficulty == 'easy':
    ## easy mode 실행
    easy_mode()
elif Choose_a_difficulty == 'hard':
    ## hard mode 실행 
    hard_mode()
else:
    print("잘못 입력하셨으므로 프로그램 종료하겠습니다.")
