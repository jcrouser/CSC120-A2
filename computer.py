class Computer:

    # What attributes will it need?
    decription:str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int



    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor_type, hard_drive_capacity, memory, operating_system, year_made, price) :
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    # What methods will you need?
        
    #updating the price of the computer
    def update_price (self, new_price):
        self.price= new_price
    
    #updating the operation #computer 
    def update_computer_OS(self,computer_os):
        self.computer =  computer_os

    

    