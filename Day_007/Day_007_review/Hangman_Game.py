import random
from Hangman_words import word_list

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

# blank = " ".join(blank_word)
# 빈 값 리스트 만들기
blank_word = []

def generate_blanks():
  for i in range(len(random_word)):
    blank_word.append("_")



# 단어가 맞았는지 틀렸는지 확인 여부 

# 랜덤으로 단어 선택
random_word = random.choice(word_list)
random_word_list = list(random_word)

generate_blanks()

print(f"""
    {logo}
""")
life = 6
while True:

  Guess_letter = input("Guess a letter: ")

  for i in range(len(random_word)):
    
    if random_word_list[i] == Guess_letter:
      if blank_word[i] == Guess_letter:
        print(f"You've already guessed {Guess_letter}.")
      blank_word[i] = Guess_letter
      
      
    elif Guess_letter not in random_word_list: 
      print(f"you  guessed {Guess_letter}, that's not in the word. You lose a life")
      life = life - 1
      break

  print(" ".join(blank_word))
  
  print(stages[life])
  if "_" not in blank_word:
    print("you win!!")
    break
  if life == 0:
    print("you die")
    break




  