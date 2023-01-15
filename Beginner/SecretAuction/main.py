from art import logo
import os

another_bidder_option = ["yes", "no"]

bidders = {}
highest_bid = 0

more_bidders = True
while more_bidders:
    print(logo)
    name = input("What is your name?: ")
    bid = int(input("What is your bid amount?: $"))
    another_bidder = input(
        "Is there another bidder? Enter 'yes' or 'no': ").lower()
    bidders[name] = bid
    while another_bidder not in another_bidder_option:
        print("You must enter 'yes' or 'no'..")
        another_bidder = input(
            "Is there another bidder? Enter 'yes' or 'no': ")
    if another_bidder == 'no':
        more_bidders = False
    os.system("clear")

for bidder in bidders:
    bid = bidders[bidder]
    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = bidder

print(logo)
print(
    f"The winner of the auction is {highest_bidder} with a bid of ${highest_bid}.")
