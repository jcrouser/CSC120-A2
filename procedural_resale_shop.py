"""
   Filename: procedural_resale_shop.py
Description: an example of procedural code to run a small computer resale shop,
             part of A2: Object-ification, CSC120: Object-Oriented Programming
             as taught at Smith College in Spring 2025. Based on an example by Sami Islam.
     Author: R. Jordan Crouser (@jcrouser)
       Date: 1 February 2024
       
       Note: YOU DO NOT NEED TO MODIFY THIS FILE
"""
# Import a few useful containers from the typing module
from typing import Dict, Optional

""" inventory: a list where we'll store our inventory """
inventory : list = []

"""
Takes in a Dict containing all the information about a computer,
adds it to the inventory, returns the assigned item_id
"""
def buy(computer: Dict):
    inventory.append(computer)
    return inventory.index(computer)

"""
Takes in an item_id and a new price, updates the price of the associated
computer if it is the inventory, prints error message otherwise
"""
def update_price(item_id: int, new_price: int):
    if inventory[item_id] is not None:
        inventory[item_id]["price"] = new_price
    else:
        print("Item", item_id, "not found. Cannot update price.")

"""
Takes in an item_id, removes the associated computer if it is the inventory, 
prints error message otherwise
"""
def sell(item_id: int):
    if inventory[item_id] is not None:
        inventory.pop(item_id)
        print("Item", item_id, "sold!")
    else: 
        print("Item", item_id, "not found. Please select another item to sell.")

"""
prints all the items in the inventory (if it isn't empty), prints error otherwise
"""
def print_inventory():
    # If the inventory is not empty
    if inventory:
        # For each item
        for item in inventory:
            # Print its details
            print(f'Item ID: {inventory.index(item)} : {item}')
    else:
        print("No inventory to display.")

def refurbish(item_id: int, new_os: Optional[str] = None):
    if inventory[item_id] is not None:
        computer = inventory[item_id] # locate the computer
        if int(computer["year_made"]) < 2000:
            computer["price"] = 0 # too old to sell, donation only
        elif int(computer["year_made"]) < 2012:
            computer["price"] = 250 # heavily-discounted price on machines 10+ years old
        elif int(computer["year_made"]) < 2018:
            computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
        else:
            computer["price"] = 1000 # recent stuff

        if new_os is not None:
            computer["operating_system"] = new_os # update details after installing new OS
    else:
        print("Item", item_id, "not found. Please select another item to refurbish.")

def main():
    buy({"description":"2019 MacBook Pro", "processor_type":"Intel", "hard_drive_capacity":256, "memory":16, "operating_system":"High Sierra", "year_made":2019, "price":1000})
    print_inventory()

main()