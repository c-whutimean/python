cells = input("Enter cells: ")
print(f""" ---------
| {cells[0]} {cells[1]} {cells[2]} |
| {cells[3]} {cells[4]} {cells[5]} |
| {cells[6]} {cells[7]} {cells[8]} |
--------- """)

check_row_1 = [cells[i] for i in range(3)]
check_row_2 = [cells[i] for i in range(3, 6)]
check_row_3 = [cells[i] for i in range(6, 9)]
across_win = [check_row_1, check_row_2, check_row_3]

check_col_1 = [cells[i] for i in range(0, 9, 3)]
check_col_2 = [cells[i] for i in range(1, 10, 3)]
check_col_3 = [cells[i] for i in range(2, 11, 3)]
down_win = [check_col_1, check_col_2, check_col_3]

check_diag_1 = [cells[i] for i in range(0, 12, 4)]
check_diag_2 = [cells[i] for i in range(2, 8, 2)]
diag_win = [check_diag_1, check_diag_2]

wins = -1
x_wins = 0
o_wins = 0
x_count = 0
o_count = 0
_count = 0
entire_board = [across_win, down_win, diag_win]
each_one = [line for section in entire_board for line in section]

for current in each_one:
    if current == ['X', 'X', 'X']:
        x_wins += 1
    elif current == ['O', 'O', 'O']:
        o_wins += 1
    else:
        wins = 0
    for char in current:
        if char == 'X':
            x_count += 1
        elif char == 'O':
            o_count += 1
        elif char == '_':
            _count += 1

"""
FOR DEBUGGING

print('wins=', wins)
print('x_wins=', x_wins)
print('o_wins=', o_wins)
print('x_count= ', x_count)
print('o_count=', o_count)
"""

if x_wins == o_wins and wins == -1 or ((x_count - o_count >= 2 or o_count - x_count >= 2) and _count > 0):
    print("Impossible")
elif _count > x_count or _count > o_count:
    print("Game not finished")
elif x_wins == 1:
    print("X wins")
elif o_wins == 1:
    print("O wins")
elif wins == 0:
    print("Draw")
