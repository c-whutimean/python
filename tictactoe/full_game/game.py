x_coord = 0
y_coord = 0
turn = 0
win = -1

b = [[' ' for i in range(9)],
     [' ' for i in range(9)],
     [' ' for i in range(9)],
     [' ' for i in range(9)],
     [' ' for j in range(9)]
    ]

print(f"""---------
| {b[1][3]} {b[2][3]} {b[3][3]} |
| {b[1][2]} {b[2][2]} {b[3][2]} |
| {b[1][1]} {b[2][1]} {b[3][1]} |
--------- """)

def check_rows():
    global win
    row_1 = [b[i][3] for i in range (1, 4)]
    row_2 = [b[i][2] for i in range(1, 4)]
    row_3 = [b[i][1] for i in range(1, 4)]
    rows = [row_1, row_2, row_3]

    for row in rows:
        if row == ['X', 'X', 'X']:
            print("X wins")
            win = 1
        elif row == ['O', 'O', 'O']:
            print("O wins")
            win = 1

def check_columns():
    global win
    col_1 = [b[1][i] for i in range(1, 4)]
    col_2 = [b[2][i] for i in range(1, 4)]
    col_3 = [b[3][i] for i in range(1, 4)]
    cols = [col_1, col_2, col_3]

    for col in cols:
        if col == ['X', 'X', 'X']:
            print("X wins")
            win = 1
        elif col == ['O', 'O', 'O']:
            print("O wins")
            win = 1

def check_diags():
    global win
    diag_1 = [b[1][3], b[2][2], b[3][1]]
    diag_2 = [b[3][3], b[2][2], b[1][1]]
    diags = [diag_1, diag_2]
    for diag in diags:
        if diag == ['X', 'X', 'X']:
            print("X wins")
            win = 1
        elif diag == ['O', 'O', 'O']:
            print("O wins")
            win = 1

def check_coord(coord):
    global x_coord
    global y_coord
    global turn
    global win

    if coord.replace(" ", "").isnumeric() == False:
        print("You should enter numbers!")
    else:
        x, y = coord.split()
        if int(x) > 3 or int(y) > 3:
            print("Coordinates should be from 1 to 3!")
        else:
            x_coord = int(x)
            y_coord = int(y)
            if b[x_coord][y_coord] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                turn += 1
                if turn < 9:
                    place_coord(x_coord, y_coord, turn)
                elif turn == 9:
                    place_coord(x_coord, y_coord, turn)
                    win = 0

def place_coord(x, y, turn):
    global b

    if turn % 2 == 0:
        b[x][y] = 'O'
    else:
        b[x][y] = 'X'

    print(f"""---------
| {b[1][3]} {b[2][3]} {b[3][3]} |
| {b[1][2]} {b[2][2]} {b[3][2]} |
| {b[1][1]} {b[2][1]} {b[3][1]} |
--------- """)

while True:
    coord = input("Enter the coordinates: ")
    check_coord(coord)
    check_rows()
    check_columns()
    check_diags()
    if win == 1:
        break
    elif win == 0:
        print("Draw")
        break

