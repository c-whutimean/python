# I could probably create functions instead of using conditional statements

money = 550
water = 400
milk = 540
beans = 120
cups = 9


def supply_list(mo, w, m, b, c):
    print("The coffee machine has:")
    print(w, "of water")
    print(m, "of milk")
    print(b, "of coffee beans")
    print(c, "of disposable cups ")
    print(mo, "of money")


def supply_levels(sign, mo, w, m, b, c):
    global money
    global water
    global milk
    global beans
    global cups

    if sign == '-':
        money = money + mo
        water = water - w
        milk = milk - m
        beans = beans - b
        cups = cups - 1
        supply_list(money, water, milk, beans, cups)
    elif sign == '+':
        money = money + mo
        water = water + w
        milk = milk + m
        beans = beans + b
        cups = cups + c
        supply_list(money, water, milk, beans, cups)

supply_list(money, water, milk, beans, cups)
action = input("\nWrite action (buy, fill, take):\n> ")

if action == "buy":
    coffee = int(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n> "))

    if coffee == 1:
        supply_levels('-', 4, 250, 0, 16, 0)
    elif coffee == 2:
        supply_levels('-', 7, 350, 75, 20, 0)
    elif coffee == 3:
        supply_levels('-', 6, 200, 100, 12, 0)

elif action == "fill":
    n_water = int(input("Write how many ml of water do you want to add:\n> "))
    n_milk = int(input("Write how many ml of milk do you want to add:\n> "))
    n_beans = int(input("Write how many grams of coffee beans do you want to add:\n> "))
    n_cups = int(input("Write how many disposable cups of coffee do you want to add:\n> "))
    print()
    supply_levels('+', 0, n_water, n_milk, n_beans, n_cups)
elif action == "take":
    print("I gave you ${}\n".format(money))
    supply_list(0, water, milk, beans, cups)

