class Computer:

    # What attributes will it need?

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    # constructor for computer class
    def __init__(self, description: str, processor: str, hard_drive_capacity: int, memory: int, operating_system: str, year_made: int, price: int):
        self.description = description
        self.processor_type = processor
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price


    def update_price1(self, new_price: int):
        self.price = new_price
