# Shortened code
# Decided to go from most to least expensive
# Score 3/4: "Too complex function. You can figure out how to simplify this code or split it into a set of small functions / methods. 
# It will make your code easy to understand and less error prone."

chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769
money = int(input())

if money >= sheep:
    if money > sheep * 2:
        print(money // sheep, "sheep")
    else:
        print("1 sheep")
elif money >= cow:
    if money > cow * 2:
        print(cow // money, "cows")
    else:
        print("1 cow")
elif money >= pig:
    if money > pig * 2:
        print(money // pig, "pigs")
    else:
        print("1 pig")
elif money >= goat:
    if money > goat * 2:
        print(money // goat, "goats")
    else:
        print("1 goat")
elif money >= chicken:
    if money > chicken * 2:
        print(money // chicken, "chickens")
    else:
        print("1 chicken")
else:
    print("None")




