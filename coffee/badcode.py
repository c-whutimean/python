'''
Terrible code :( needs much improvement on excessive usage of conditional statements
Will return to clean up code
'''

water = int(input("Write how many ml of water the coffee machine has:\n> "))
milk = int(input("Write how many ml of milk the coffee machine has:\n> "))
beans = int(input("Write how many grams of coffee beans the coffee machine has:\n> "))
cups = int(input("Write how many cups of coffee you will need:\n> "))

n_water = cups * 200
n_milk = cups * 50
n_beans = cups * 15

if water == 0 or milk == 0 or beans == 0:
    if cups > 0:
        print("No, I can only make 0 cups of coffee")
    else:
        print("Yes, I can make that amount of coffee")
elif n_water <= water and n_milk <= milk and n_beans <= beans:
    water = water - n_water
    milk = milk - n_milk
    beans = beans - n_beans

    if water >= 200 and milk >= 50 and beans >= 15:
        w = water // 200
        m = milk // 50
        b = beans // 15
        amount = [w, m, b]

        print("Yes, I can make that amount of coffee (and even", min(amount), "more than that)")
    else:
        print("Yes, I can make that amount of coffee")
elif n_water > water or n_milk > milk or n_beans > beans:
    if water >= 200 and milk >= 50 and beans >= 15:
        w = water // 200
        m = milk // 50
        b = beans // 15
        amount = [w, m, b]

        print("No, I can make only", min(amount), "cups of coffee")
