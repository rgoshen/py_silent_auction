from replit import clear
from art import logo

print(logo)

bidding_finished = False
bids = {}

def find_winning_bid(bidding_record):
    highest_bid = 0
    winner = ""

    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid:.2f}")

while not bidding_finished:
    name = input("What is your name?: ").title()
    price = float(input("What is your bid?: $"))
    should_close = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    bids[name] = price

    if should_close == "no":
        bidding_finished = True
        print("Auction is closed.")
        find_winning_bid(bids)
    elif should_close == "yes":
        clear()
    else:
        ask_again = input("I didn't understand.  Type 'yes' or 'no'.\n")
        if ask_again == "no":
            bidding_finished = True
            print("Auction is closed.")
            find_winning_bid(bids)            
