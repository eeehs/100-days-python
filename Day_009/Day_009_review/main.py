from art import logo

print(logo)

print("Welcome to the secret auction program.")

auction ={}
bid = 0
winner = ""
while True:
    name = input("What is your name?: ")
    bids = int(input("What's your bid?: $"))
    auction[name] = bids
    for a in auction.keys():
        if auction[a] > bid:
            bid = auction[a]
            winner = a 

    any_other = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if any_other == "yes":
        continue
    else:
        print(f"The winner is {winner} with a bid of &{bid}")