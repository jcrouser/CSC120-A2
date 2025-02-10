from computer import *

class ResaleShop:

    # What attributes will it need?

    inventory = []

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

    # What methods will you need?s

    def buy(self, description: str, processor: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        # 1. call Comp(...) construtor to
        # create new comp instance
        
        new_computer = Computer(description, processor, hard_drive_capacity, memory, operating_system, year_made, price)

        # 2. call inventory.append(..) to add the 
        # new Computer instance to the inventory
        self.inventory.append(new_computer)

    

    def sell(self, item_id: int):
        if self.inventory[item_id] is not None:
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")


    #Update the price of the computer 
    def update_price(self, item_id: int, new_price: int):
        if self.inventory[item_id] is not None:
            self.inventory[item_id].update_price1(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")
        


    def refurbish(self, item_id:int):
        if self.inventory[item_id] is not None:
            computer = self.inventory[item_id] # locate the computer
        if int(computer["year_made"]) < 2000:
            computer["price"] = 0 # too old to sell, donation only
        elif int(computer["year_made"]) < 2012:
            computer["price"] = 250 # heavily-discounted price on machines 10+ years old
        elif int(computer["year_made"]) < 2018:
            computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
        else:
            computer["price"] = 1000 # recent stuff

        if self.new_os is not None:
            computer["operating_system"] = self.new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
    

    def print_inventory(self):
    # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(f'Item ID: {self.inventory.index(item)} : {item.description}, ')
        else:
            print("No inventory to display.")

    
if __name__ == "__main__": 
    shop = ResaleShop()
    shop.buy("good", "fast", 2, 15, "mac", 2000, 50)
    shop.print_inventory()
    shop.update_price(0, 2)
