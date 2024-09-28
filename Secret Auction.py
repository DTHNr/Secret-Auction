print(
    """
                         ___________
                         \         /
                          )_______(
                          |-------|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )-------(
                         ._________.
                         `'-------'`
                       .-------------.
                      ._______________.
    
"""
)

bidders_info = {}

def secret_auction_program():
    name = input("What is your name?: ").title()
    bid = int(input("What is your bid?: "))
    bidders_info[name] = bid
    
    additional_bidder = input("Are there any other bidders? Type \'yes\' or \'no\': ").lower()
    if additional_bidder == "yes":
        print("\n" * 100)
        secret_auction_program()
    else:
        new_value = 0
        new_key = ""
        for bidder in bidders_info:
            key_name = bidder
            value = bidders_info[key_name]
            if value > new_value:
                new_value = value
                new_key = key_name
        print(f"The winner is: {new_key}")
        print(f"Bid ammount: {new_value}")

secret_auction_program()
