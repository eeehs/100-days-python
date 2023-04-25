#TODO 1. Create a dictionary in this format:
import csv
import pandas
with open("./NATO-alphabet/nato_phonetic_alphabet.csv") as file:
    data = csv.reader(file)
    print(data)
    nato_dic = {letter:code for letter,code in data if letter != "letter"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

words = input("Enter a word: ").upper()
word = [nato_dic[w] for w in words]
print(word)