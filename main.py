# Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union
from computer import ComputerClass 
# Import the functions we wrote in procedural_resale_shop.py
from oo_resale_shop import ResaleShop
""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""
def main():
    
    # First, let's make a computer
    computer_object = ComputerClass.create_computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )

    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)
    
    # creating an instance of ResaleShop
    inventory = {} 
    resale_shop = ResaleShop(inventory)
    
    # Add it to the resale store's inventory
    print("Buying", computer_object["description"])
    print("Adding to inventory...")
    computer_id = resale_shop.buy(computer_object)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resale_shop.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    ComputerClass.refurbish(computer_id, new_OS, inventory)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resale_shop.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    resale_shop.sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    resale_shop.print_inventory()
    print("Done.\n")

# Calls the main() function when this file is run
if __name__ == "__main__": main()
