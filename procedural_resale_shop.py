"""
   Filename: procedural_resale_shop.py
Description: an example of procedural code to run a small computer resale shop,
             part of A2: Object-ification, CSC120: Object-Oriented Programming
             as taught at Smith College in Fall 2022. Based on an example by Sami Islam.
     Author: R. Jordan Crouser (@jcrouser)
       Date: 11 September 2022
       
       Note: YOU DO NOT NEED TO MODIFY THIS FILE
"""
# Import a few useful containers from the typing module
from typing import Dict, Union, Optional

""" inventory: a dictionary where we'll store our inventory
    The key is an int representing the item number
    The value is another dictionary containing information about the machine
"""
inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {}

itemID = 0 # We'll increment this every time we add a new item 
           # so that we always have a new value for the itemID

"""
Takes in a Dict containing all the information about a computer,
adds it to the inventory, returns the assigned item_id
"""
def buy(computer: Dict[str, Union[str, int, bool]]):
    global itemID
    itemID += 1 # increment itemID
    inventory[itemID] = computer
    return itemID

"""
Takes in an item_id and a new price, updates the price of the associated
computer if it is the inventory, prints error message otherwise
"""
def update_price(item_id: int, new_price: int):
    if item_id in inventory:
        inventory[item_id]["price"] = new_price
    else:
        print("Item", item_id, "not found. Cannot update price.")

"""
Takes in an item_id, removes the associated computer if it is the inventory, 
prints error message otherwise
"""
def sell(item_id: int):
    if item_id in inventory:
        del inventory[item_id]
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
        for item_id in inventory:
            # Print its details
            print(f'Item ID: {item_id} : {inventory[item_id]}')
    else:
        print("No inventory to display.")

def refurbish(item_id: int, new_os: Optional[str] = None):
    if item_id in inventory:
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