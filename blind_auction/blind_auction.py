# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art


bidders ={}

print(art.logo)
while True:
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    add_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")

    bidders[name] = int(bid)
    print("\n" * 20)
    if add_bidders.lower().strip() == "no":
        winner = max(bidders,key=bidders.get)
        print(f"The winner is {winner} with a bid of ${bidders[winner]}")
        break



