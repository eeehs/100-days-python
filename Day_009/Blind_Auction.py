from art import logo

print(logo)
print("Welcome to the secret auction program.")

aution = {}

while True:

    aution_name = input("What is your name? ")
    print("")
    aution_bid = int(input("what's your bid? $"))
    print("")
    aution[aution_name] = aution_bid

    continue_aution = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if continue_aution == "yes":
        continue
    else:
        break

# aution 가격 계산
winner = ""
winner_bid = 0
for key in aution:
    if aution[key] > winner_bid:
        winner = key
        winner_bid = aution[key]

print("")
print(f"The winner is {winner} with a bid of ${winner_bid}")