water = int(input("Write how many ml of water the coffee machine has:"))
milk = int(input("Write how many ml of milk the coffee machine has:"))
coffee = int(input("Write how many grams of coffee beans the coffee machine has:"))
cups = int(("Write how many cups of coffee you will need:"))
cup_coffee = water // 200
cup_milk = milk // 50
cup_coffee_beans = coffee // 15
cup_coffee = min(cup_coffee, cup_milk, cup_coffee_beans)
if cups == cup_coffee:
    print("Yes, I can make that amount of coffee")
elif cups > cup_coffee:
    print("No, I can make only", cup_coffee, "cups of coffee")
elif cups < cup_coffee:
    print("Yes, I can make that amount of coffee (and even", cup_coffee - cups, "more than that)")


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
