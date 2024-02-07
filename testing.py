from computer import Computer 
from oo_resale_shop import ResaleShop

#creating atestcomputer
def main():
    testcomputer= Computer("Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500)
    
    #printing description of the testcomputer
    print(testcomputer.description)

    #creating a shop named walmart
    store_testing = ResaleShop("walmart")

    #printing initial inventory of the store
    print(store_testing.inventory)

    #buying the test computer and adding it to the inventory of the store
    store_testing.buying_computer (testcomputer)
    print(store_testing.inventory)

    #printing the name of the store
    print(store_testing.store)

    #printing the description of the computer in the inventory of the store
    print(store_testing.inventory[0].description)

    #refurbishing and prinnting the test computer and its price
    store_testing.refurbishing_computer(testcomputer)
    print(testcomputer.price) 

if __name__ == "__main__": main()
