import art

# Print the auction logo (assuming `art.logo` is defined correctly in the `art` module)
print(art.logo)


# Function to determine the highest bidder
def highest_bidder(bidder_values):
    winner = ""
    highest_bid_amt = 0
    for bidder in bidder_values:
        bid_amt = bidder_values[bidder]
        if bid_amt > highest_bid_amt:
            highest_bid_amt = bid_amt
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid_amt}")


# Dictionary to store bidder data
bidders = {}
continue_bidding = True

while continue_bidding:
    # Collecting user input
    name = input("What is your name? ")
    price = int(input("What is your bid?: $"))

    # Add the bid to the dictionary
    bidders[name] = price

    # Check if there are more bidders
    extra = input("Are there any other bidders? Type 'yes' or 'no': ").strip().lower()
    if extra == 'no':
        continue_bidding = False
        highest_bidder(bidders)
    elif extra == 'yes':
        print("\n" * 50)  # Simulate clearing the screen
    else:
        print("Invalid input. Assuming no more bidders.")
        continue_bidding = False
        highest_bidder(bidders)
