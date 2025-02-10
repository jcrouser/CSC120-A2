from computer import *
from typing import Optional


class ResaleShop:

    inventory = []

    def __init__(self):
        self.inventory = []


    # takes in a new computer instance and adds it to the inventory
    def buy(self, description: str, processor: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):   
        new_computer = Computer(description, processor, hard_drive_capacity, memory, operating_system, year_made, price)
        self.inventory.append(new_computer)

    
    # Removes a computer from the inventory 
    def sell(self, item_id: int):
        if self.inventory[item_id] is not None:
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")



        

    # Updates the price of the computer 
    def update_price(self, item_id: int, new_price: int):
        if self.inventory[item_id] is not None:
            self.inventory[item_id].update_price1(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")
        

    # checks the age of the computer and discounts accordingly
    # checks and updates the operating system
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if self.inventory[item_id] is not None:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.update_price(0) # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.update_price1(250) # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.update_price(550) # discounted price on machines 4-to-10 year old machines
            else:
                computer.update_price(1000) # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
    
    # prints the inventory
    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(f'Item ID: {self.inventory.index(item)} : {item.description}, {item.processor_type}, {item.hard_drive_capacity}, {item.memory}, {item.operating_system}, {item.year_made}, {item.price}  ')
        else:
            print("No inventory to display.")

    
if __name__ == "__main__": 
     shop = ResaleShop()
     shop.buy("good", "fast", 2, 15, "mac", 2000, 50)
     shop.print_inventory()
     shop.sell(0)
     shop.print_inventory()
     shop.buy("good", "fast", 2, 15, "mac", 2000, 50)
     shop.print_inventory()
     shop.update_price(0, 100)
     shop.print_inventory()
     shop.refurbish(0, "lux")
     shop.print_inventory()




