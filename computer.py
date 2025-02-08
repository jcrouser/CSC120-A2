class Computer:

    # What attributes will it need?

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int


    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, description, processor, hdc, memory, os, year, amt: float):
        self.description = description
        self.processor_type = processor
        self.hard_drive_capacity = hdc
        self.memory = memory
        self.operating_system = os
        self.year_made = year
        self.price = amt


        #pass # You'll remove this when you fill out your constructor

    # What methods will you need?

    def update_os(self):
        pass
