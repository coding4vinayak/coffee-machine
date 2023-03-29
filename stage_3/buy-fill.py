water = int(input("Write how many ml of water the coffee machine has:"))
milk = int(input("Write how many ml of milk the coffee machine has:"))
coffee = int(input("Write how many grams of coffee beans the coffee machine has:"))
cups = int(input("Write how many cups of coffee you will need:"))

cup_coffee = water // 200
cup_milk = milk // 50
cup_coffee_beans = coffee // 15
cup = min(cup_coffee, cup_milk, cup_coffee_beans)

if cups == cup:
    print("Yes, I can make that amount of coffee")
elif cups > cup:
    print("No, I can make only", cup, "cups of coffee")
else:
    print("Yes, I can make that amount of coffee (and even", cup - cups, "more than that)")


def status (water, milk, coffee, cups, money):
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(coffee, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")
    print()

def standerd_input(buy , fill , take):
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "exit":
        exit()
    
def buy(espresso, latte, cappuccino):
    print("choose your coffee (espresso, latte, cappuccino):")
    action = input()
    if acttion == "expresso":
        espresso()
    elif action == "latte":
        latte()
    elif action == "cappuccino":
        cappuccino()
    else:
        print("please choose one of the coffee")
        buy(espresso, latte, cappuccino)

def espresso(water, milk, coffee, cups, money):
    water -= 250
    coffee -= 16
    cups -= 1
    money += 4
    status(water, milk, coffee, cups, money)
    standerd_input(buy, fill, take)

def latte(water, milk, coffee, cups, money):
    water -= 350
    milk -= 75
    coffee -= 20
    cups -= 1
    money += 7
    status(water, milk, coffee, cups, money)
    standerd_input(buy, fill, take)

def cuppuccino(water, milk, coffee, cups, money):
    water -= 200
    milk -= 100
    coffee -= 12
    cups -= 1
    money += 6
    status(water, milk, coffee, cups, money)
    standerd_input(buy, fill, take)

def fill(water, milk, coffee, cups):
    water = int(input("Write how many ml of water the coffee machine has:"))
    milk = int(input("Write how many ml of milk the coffee machine has:"))
    coffee = int(input("Write how many grams of coffee beans the coffee machine has:"))
    cups = int(input("Write how many cups of coffee you will need:"))
    status(water, milk, coffee, cups, money)
    standerd_input(buy, fill, take)

def take(money):
    print("I gave you $", money)
    money = 0
    status(water, milk, coffee, cups, money)
    standerd_input(buy, fill, take)

water = 400
milk = 540
coffee = 120
cups = 9
money = 550
status(water, milk, coffee, cups, money)
standerd_input(buy, fill, take)
