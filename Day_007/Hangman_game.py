from hangman_art import logo, stages
from hangman_words import word_list
import random
print(logo)

# 팩맨 수명 
life = 6

# 무작위 문자 
random_word = random.choice(word_list)

# 문자에 맞는 빈 문자열들 생성
quiz_word = []

for i in range(0,len(random_word)):
    quiz_word.append("_")

# 잠시 콜론
# quiz_word = " ".join(quiz_word)    


# 팩맨 게임 
def Guess():
    global life
    global Game
    if Guess_letter in random_word:
        if Guess_letter in quiz_word:
            print(f"You've already guessed {Guess_letter}\n")
            print(" ".join(quiz_word))
            print(stages[life])
        else:
            for i in range(0, len(random_word)):
                if random_word[i] == Guess_letter:
                    quiz_word[i] = Guess_letter
            print(" ".join(quiz_word))
            print(stages[life])
            if "_" not in quiz_word:
                Game = False
                print("You win")
    else:
        print(f"you guessed {Guess_letter}, that's not in the word. You lose life.")
        print(" ".join(quiz_word))
        life -= 1
        print(stages[life])
        if life == 0:
            Game = False
            print("You lose")

# Main
Game = True
while Game:
    Guess_letter = input("Guess a letter: ")
    Guess()

