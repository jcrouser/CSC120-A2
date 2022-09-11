# Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union

# Import the functions we wrote in procedural_computer_shop.py
from procedural_computer_shop import buy, update_price, sell, print_inventory

# # Import the functions we wrote in procedural_resale_shop.py, renaming them with an 'r' prefix
from procedural_resale_shop import buy as rbuy, update_price as rupdate_price, sell as rsell, print_inventory as rprint_inventory, refurbish

""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""
def create_computer(description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
    return {'description': description,
            'processor_type': processor_type,
            'hard_drive_capacity': hard_drive_capacity,
            'memory': memory,
            'operating_system': operating_system,
            'year_made': year_made,
            'price': price
    }

def main():
    
    # First, let's make a computer
    computer = create_computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    # Print a little banner
    print("-" * 14)
    print("COMPUTER STORE")
    print("-" * 14)

    # Then we'll add it to the computer store's inventory
    print("Buying", computer["description"])
    print("Adding to inventory...")
    computer_id = buy(computer)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")

    # Update price
    new_price = int(computer["price"] * 0.8) # discount to 80% of original price
    print("New price for Item ID:", computer_id, "=", new_price)
    print("Updating inventory...")
    update_price(computer_id, new_price)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    print_inventory()
    print("Done.\n")

    # We could do the same thing with the resale store:

    # Print another little banner
    print("-" * 12)
    print("RESALE STORE")
    print("-" * 12)

    # Add it to the resale store's inventory
    print("Buying", computer["description"])
    print("Adding to inventory...")
    computer_id = rbuy(computer)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    rprint_inventory()
    print("Done.\n")

    # This time, we'll refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    refurbish(computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    rprint_inventory()
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": main()