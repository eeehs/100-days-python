alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction in ['encode','decode']:
            text = input("Type your message:\n").lower()
            shift = int(input("Type the shift number:\n"))
            result = ""

            if direction == "encode":
                for i in text:
                    text_index = alphabet.index(i) + shift
                    if text_index > alphabet.index("z"):
                        text_index = text_index - 26
                    result += (alphabet[text_index])
                print(f"Here's the {text} result: {result}")
            elif direction == "decode":
                for i in text:
                    text_index = alphabet.index(i) - shift
                    result += (alphabet[text_index])
                print(f"Here's the {text} result: {result}")
            
            continue_caesar_ciper = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")

            if continue_caesar_ciper == "yes":
                pass
            else:
                break     
    else:
        print("제대로 입력하세요.")


    



