import opcode
from oo_resale_shop import ResaleShop

class ComputerClass:

    # What attributes will it need?

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description:str, processor_type: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
            self.description = description 
            self.processor_type = processor_type
            self.hard_drive_capacity = hard_drive_capacity
            self.memory = memory
            self.operating_system = operating_system
            self.year_made = year_made
            self.price = price
            
    # What methods will you need?
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
            'price': price}

    def refurbish(self, item_id: int, new_os:str = None, inventory={}):
        """ 
        Decides price of items based on the year the computer was made. Also updates the operating system if viable. 
        """
        if item_id in inventory:
            computer = inventory[item_id] # locate the computer
            if self.year_made < 2000:
                self.price = 0 # too old to sell, donation only
            elif self.year_made < 2012:
                self.price = 250 # heavily-discounted price on machines 10+ years old
            elif self.year_made < 2018:
                self.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                self.price = 1000 # recent stuff

            if self.new_os is not None:
                self.operating_system = self.new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")