from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

while True:

    code = input("Type 'encode' to encrypy, type 'decode' to decrypt: ")
    messages = list(input("Type your message: "))
    shift_number = int(input("Type the shift number: "))
    result = []

    if code == 'encode':
        for message in messages:
            x = alphabet.index(message) + shift_number
            result.append(alphabet[x])
            results = (''.join(result))
        print(f"Here's the encoded result: {results}")
    elif code == 'decode':
        for message in messages:
            x = alphabet.index(message) - shift_number
            result.append(alphabet[x])
            results = (''.join(result))
        print(f"Here's the decoded result: {results}")
    yes_or_no = input("Type 'yes' if you want to go again. Otherwise type 'no'. ")
    if yes_or_no == 'yes':
        continue
    else:
        print("Goodbye")
        break