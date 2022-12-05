student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    pass

import pandas,csv
student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
alphabet = pandas.read_csv(".\\Day_026\\nato_phonetic_alphabet.csv")
alphabet_dataframe = pandas.DataFrame(alphabet)
#TODO 1. Create a dictionary in this format:
alphabet_dict = {row.letter:row.code for (index,row) in alphabet_dataframe.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

output_list = [alphabet_dict[letter] for letter in word]
print(output_list)