# blind_auction.py

# Updated ASCII art logo
logo = r"""
                          ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
"""

print(logo)
print("Welcome to the Blind Auction!\n")

# Dictionary to store bids
bids = {}

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder, amount in bidding_record.items():
        if amount > highest_bid:
            highest_bid = amount
            winner = bidder
    return winner, highest_bid

auction_running = True

while auction_running:
    name = input("What is your name? ")
    bid_input = input("What is your bid? R ")

    try:
        bid = float(bid_input)
    except ValueError:
        print("Invalid bid amount. Please enter a number.")
        continue

    bids[name] = bid

    more_bidders = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()
    if more_bidders == "yes":
        print("\n" * 50)
        print(logo)
        print("Next bidder, please...\n")
    elif more_bidders == "no":
        auction_running = False
    else:
        print("Input not recognized, ending auction.")
        auction_running = False

winner, highest_bid = find_highest_bidder(bids)

print("\nAuction complete!")
print(f"The winner is {winner} with a bid of R {highest_bid:.2f}.")
