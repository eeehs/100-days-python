#Step 1 

import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
A = random.choice(word_list)
A_list = list(random.choice(word_list))


#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


B = input("Guess a letter: ").lower()


for i in range(len(A)):
    if B == A[i]:
        print("Right")
    else:
        print("Wrong")
