import random

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


word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
chosen_word_list = list(random.choice(word_list))

print(f'Pssst, the solution is {chosen_word}.')

display_list = []
for e in range(len(chosen_word)):
    display_list.append("_")

life = 6
n = 0
while not (n == len(chosen_word)):
    guess = input("Guess a letter: ").lower()
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            if display_list[i] == "_": 
                display_list[i] = guess
                n = n + 1
    if guess not in display_list:
        life = life - 1 
        if life == 0:
            print(stages[life])
            print("You die")
            break
    print(display_list)
    print(stages[life])
    
 
