# TASK 3: SILENT AUCTION

from art import logo

print(logo)

auction = {}
game_over = False

while not game_over:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    auction[name] = bid
    other_bidders = input("Are there any other bidders? type 'yes' or 'no': ").lower()
    if other_bidders != 'yes':
        game_over = True
    else:
        print("\n" * 45)
        game_over = False

max_bid = 0
bidder_name = ""
for key in auction:
    if (auction[key]) > max_bid:
        bidder_name = key
        max_bid = auction[key]

print(f"The winner is {bidder_name} with a bid of ${max_bid}")
        