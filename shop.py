'''
CandyShop
'''

from uuid import uuid4
from time import sleep

# Helpers
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# Global
inventory = []


class Candy():
    def __init__(self, name, producer, price, sugar_level):
        self.name = name
        self.producer = producer
        self.price = price
        self.sugar_level = sugar_level
        self.id = str(uuid4())

        inventory.append(self)

    def __repr__(self):
        return f'{self.name} by {self.producer}, {self.price} EUR, with {self.sugar_level}g of sugars per 100g | ID {self.id}'

    def __str__(self):
        return f'{self.name} by {self.producer}, {self.price} EUR, with {self.sugar_level}g of sugars per 100g | ID {self.id}'


def createNewCandy():
    name = input('Write the name of the candy \n')
    producer = input('Who is making it? \n')
    price = input("What's the price? *in EUR \n")
    sugar_level = input("How much sugars there is in 100g of it? *in grams \n")
    new_candy = Candy(name, producer, price, sugar_level)
    print("Great, you've created a new candy!")
    print(new_candy)
    choose()


def showInventory():
    print("\nHere's your inventory")
    print('------------------\n')
    sleep(0.5)
    for candy in inventory:
        sleep(1)
        print(candy)
        sleep(0.5)
        print('-------')
    sleep(0.5)
    print('\n------------------')
    choose()


def choose(choose_again=False):
    if choose_again:
        print("I didn't get that, please write again")
    else:
        sleep(1)
        print('\n\nWhat do you want to do now? \n')

    print(
        f"You can write {color.BOLD}new{color.END} to create a new candy or {color.BOLD}end{color.END} to check inventory")
    sleep(1)
    choice = input("\nWhat's your choice? \n")
    if choice == 'new':
        createNewCandy()
    elif choice == 'inv':
        showInventory()
    else:
        choose(True)


print('Hello there')
sleep(1)
print('Welcome to the Candy Shop!')
sleep(1)
print("Currently there are no candies, let's create one\n")
sleep(2)

createNewCandy()
