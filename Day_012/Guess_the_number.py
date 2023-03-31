from art import logo
import random

Guess_number = random.choice(range(1,101))

# game_mode 함수
def game_mode(attempts):
    while True:
        print(f"You have {attempts} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        if guess == Guess_number:
            print(f"You got it! The answer was {Guess_number}")
            break
        elif guess > Guess_number:
            print("high\n")
            attempts -= 1
            if attempts == 0:
                print("you've run of guesses, you lose")
                break
        elif guess < Guess_number:
            print("low\n")
            attempts -= 1
            if attempts == 0:
                print("you've run of guesses, you lose")
                break

# Main
print(f"""
{logo}
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
""")

mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
if mode == "easy":
    game_mode(10)
elif mode == "hard":
    game_mode(5)
else:
    print("잘못 입력하셨습니다. 게임을 종료합니다.")

    