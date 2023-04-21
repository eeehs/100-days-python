PLACEHOLDER = "[name]"




with open("./Mail Merge/input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Mail Merge/input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    print(letter_contents)
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Mail Merge/Output/ReadyToSend/letter_for_{stripped_name}","w") as send_file:
            send_file.write(new_letter)
            

