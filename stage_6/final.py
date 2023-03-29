
def status(water, milk, coffee, cups, money):
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee} of coffee beans")
    print(f"{cups} of disposable cups")
    print(f"${money} of money")
    print()

def buy(water, milk, coffee, cups, money):
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino,  back - to main menu:")
    choice = input()
    if choice == "1":
        if water >= 250 and coffee >= 16 and cups >= 1:
            print("I have enough resources, making you a coffee!")
            water -= 250
            coffee -= 16
            cups -= 1
            money += 4
        else:
            print("Sorry, not enough resources!")
    elif choice == "2":
        if water >= 350 and milk >= 75 and coffee >= 20 and cups >= 1:
            print("I have enough resources, making you a coffee!")
            water -= 350
            milk -= 75
            coffee -= 20
            cups -= 1
            money += 7
        else:
            print("Sorry, not enough resources!")
    elif choice == "3":
        if water >= 200 and milk >= 100 and coffee >= 12 and cups >= 1:
            print("I have enough resources, making you a coffee!")
            water -= 200
            milk -= 100
            coffee -= 12
            cups -= 1
            money += 6
        else:
            print("Sorry, not enough resources!")
    elif choice == "back":
        pass
        
    else:
        print("Invalid choice!")
    return (water, milk, coffee, cups, money)

def fill(water, milk, coffee, cups):
    water += int(input("How many ml of water do you want to add?\n"))
    milk += int(input("How many ml of milk do you want to add?\n"))
    coffee += int(input("How many grams of coffee beans do you want to add?\n"))
    cups += int(input("How many disposable cups do you want to add?\n"))
    return (water, milk, coffee, cups)

def take(money):
    print(f"I gave you ${money}")
    money = 0
    return money

def main():
    water = 400
    milk = 540
    coffee = 120
    cups = 9
    money = 550

    

    while True:
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        print()

        if action == "buy":
            water, milk, coffee, cups, money = buy(water, milk, coffee, cups, money)
        elif action == "fill":
            water, milk, coffee, cups = fill(water, milk, coffee, cups)
        elif action == "take":
            money = take(money)
        elif action == "remaining":
            status(water, milk, coffee, cups, money)
        elif action == "exit":
            break
        else:
            print("Invalid action!")

if __name__ == "__main__":
    main()

#final solution