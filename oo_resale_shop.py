# Import a few useful containers from the typing module
from typing import Dict, Union, Optional
import computer
itemID = 0
class ResaleShop:

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, inventory: Dict[int, Dict[str, Union[str, int, bool]]] = {} ):
        self.inventory = inventory
        
    # What methods will you need?
    
    def buy(self,computer: Dict[str, Union[str, int, bool]]):
        """
            Takes in a Dict containing all the information about a computer,
            adds it to the inventory, returns the assigned item_id
        """
        global itemID
        itemID += 1 # increment itemID
        self.inventory[itemID] = computer
        return itemID
    
    def updateprice(self, item_id: int, new_price: int):
        """
        Takes in an item_id and a new price, updates the price of the associated
        computer if it is the inventory, prints error message otherwise
        """
        if item_id in self.inventory:
            self.inventory[item_id]["price"] = new_price 
        else:
            print("Item", item_id, "not found. Cannot update price.")

    def sell (self, item_id):    
        """
        Takes in an item_id, removes the associated computer if it is the inventory, 
        prints error message otherwise
        """
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    def print_inventory(self):
        """
        prints all the items in the inventory (if it isn't empty), prints error otherwise
        """
        def print_inventory():
            # If the inventory is not empty
            if self.inventory:
                # For each item
                for item_id in self.inventory:
                    # Print its details
                    print(f'Item ID: {item_id} : {self.inventory[item_id]}')
            else:
                print("No inventory to display.")
    
    