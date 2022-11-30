# #TODO: Create a letter using starting_letter.txt 
# #for each name in invited_names.txt
# #Replace the [name] placeholder with the actual name.
# #Save the letters in the folder "ReadyToSend".
    
# #Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# name = "[name]"
# invite_number = 0

# def starting_letter_chage():
#     with open("\\Users\\dlrb9\\OneDrive\\바탕 화면\\github\\100-days-python\\Day_024\\Mail_Merge\\Input\\Letters\\starting_letter.txt") as start_File:
#         change_letter = start_File.readlines()[0]
#         change_letter.replace(name, invited_names())
#         for i in start_File.readlines():
#             print(i)


HOLDER ="[name]"
        
with open(".\Day_024\\Mail_Merge\\Input\\Names\\invited_names.txt",encoding="utf-8") as names_file:
    names = names_file.readlines()
    
with open(".\Day_024\\Mail_Merge\\Input\\Letters\\starting_letter.txt",encoding="utf-8") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(HOLDER , stripped_name)
        with open(f".\Day_024\\Mail_Merge\\Output\\ReadyToSend\\{stripped_name}.txt",mode="w") as completed_letter:
            completed_letter.write(new_letter)

# invited_names()
# starting_letter_chage()
    

# with open("\\Users\\dlrb9\\OneDrive\\바탕 화면\\github\\100-days-python\\Day_024\\Mail_Merge\\Input\\Letters\\starting_letter.txt") as start_File:
#     start_File.readlines()[0]

# # with open("\\Users\\dlrb9\\OneDrive\\바탕 화면\\github\\100-days-python\\Day_024\\Mail_Merge\\Input\\Names\\invited_names.txt") as f:
# #     print(f.readlines())    

# with open(f"\\Users\\dlrb9\\OneDrive\\바탕 화면\\github\\100-days-python\\Day_024\\Mail_Merge\\Output\\ReadyToSend\\{new}", mode="w") as new_file:




# 파일 생성 구문 