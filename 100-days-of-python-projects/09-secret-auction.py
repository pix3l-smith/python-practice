import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("""
    ___________
    \\         /
     )_______(
     |       |_.-._,.---------.,_.-._
     |       | | |               | | ''-.
     |       |_| |_             _| |_..-'
     |_______| '-' `'---------'` '-'
     )       (
    /_________\\
    `'-------'`
  .-------------.
 /_______________\\
""")
print("Welcome to the secret auction program.")

secret_auction = {}

num_bidders = int(input("How many bidders are there? "))
for i in range(num_bidders):
    bidder_name = input("What is your name? ")
    bidder_bid = int(input("What is your bid? $"))
    secret_auction[bidder_name] = bidder_bid
    clear_screen()

secret_auction_winner = max(secret_auction, key=secret_auction.get)

print("The bids were:")
for name, bid in secret_auction.items():
    print(f"{name} - ${bid}")
print(f"The winner is:\n{secret_auction_winner.upper()}!")
