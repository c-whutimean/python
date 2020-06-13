chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769
money = int(input())

if money < chicken:
    print("None")
elif money == chicken or money < (chicken * 2):
    print("1 chicken")
elif chicken < money < goat:
    num_chickens = money // chicken
    if num_chickens == 1:
        print("1 chicken")
    print(str(num_chickens) + " chickens")
elif money == goat:
    print("1 goat")
elif goat < money < pig:
    num_goat = money // goat
    if num_goat == 1:
        print("1 goat")
    else:
        print(str(num_goat) + " goats")
elif money == pig:
    print("1 pig")
elif pig < money < cow:
    num_pig = money // pig
    if num_pig == 1:
        print("1 pig")
    else:
        print(str(num_pig) + " pigs")
elif money == cow:
    print("1 cow")
elif cow < money < sheep:
    num_cow = money // cow
    if num_cow == 1:
        print("1 cow")
    else:
        print(str(num_cow) + " cows")
elif money == sheep:
    print("1 sheep")
elif money > sheep:
    num_sheep = sheep // money
    if num_sheep == 1:
        print("1 sheep")
    else:
        print(str(num_sheep) + " sheeps")

