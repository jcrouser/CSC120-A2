class ResaleShop:
    from typing import Dict, Optional

    # What attributes will it need?
    inventory =[] # computer object will go in here

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self,store,inventory=[]):
        self.store = store
        self.inventory = inventory

    # What methods will you need?
    
    #adding computer to the inventory
    def buying_computer(self,computer):
        self.inventory.append(computer)
   
    #removing computer from the inventory
    def selling_computer(self, computer):
        self.inventory.remove(computer)

    #refurbishing computer and updating the price depending on the year it was created.
    def refurbishing_computer(self,computer, new_os: Optional[str] = None):
        if computer in self.inventory: 
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

    
    
    