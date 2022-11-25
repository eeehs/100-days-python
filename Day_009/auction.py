from art import logo
print(logo)

bids = {}
bidding_finished = False


while not bidding_finished:
    name = input("What's your name?")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or 'no'.")
    if should_continue == "no":
        bidding_finished = True
        highest_bid = 0 
        for bid in bids:
            bid_amount = bids[bid] 
            if bid_amount > highest_bid:
                highest_bid = bid_amount
print(highest_bid)


