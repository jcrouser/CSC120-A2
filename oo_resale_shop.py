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

    

    def sell(self):
        #remove a computer from the inventory 



        pass

    #Update the price of the computer 
    def update_price(self, new_amt:int):
        self.price = new_amt
        


    def refurbish(self):
        pass
    

    
