from art import logo
import random
attempt = 10
random_number = random.choice(range(1,101))

def welcome():
    print(logo)
    print("I'm thinking of a number between 1 and 100.")

def difficulty(choose_difficulty):
    global attempt
    while True:
        if choose_difficulty == 'easy':
            print(f"you have {attempt} attempts remaining to guess the number.")
            break
        else:
            attempt = attempt - 5 
            print(f"you have {attempt} attempts remaining to guess the number.")
            break
def game():
    global attempt
    while True:
        guess = int(input("Make a guess: "))
        if random_number > guess:
            attempt = attempt - 1 
            print("Too low")
            if attempt == 0 :
                print("You've run out of guesses, you lose.")
                break
            print("Guess again")
            print(f"you have {attempt} attempts remaining to guess the number")
        elif random_number == guess:
            attempt = 0  
            print(f"You got it! The answer was {random_number}")
            break
        else:
            attempt = attempt - 1 
            print("Too high")
            if attempt == 0 :
                print("You've run out of guesses, you lose.")
                break
            print("Guess again")
            print(f"you have {attempt} attempts remaining to guess the number")
        


# 게임 시작 
welcome()
# 랜덤 번호 출력
# print(f"pssst, the correct answer is {random_number}")

choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
difficulty(choose_difficulty)
game()

