"""
Adding the ability to select a cell for you move.
The following below is the list of coordinates to make a move:
  (1, 3) (2, 3) (3, 3)
  (1, 2) (2, 2) (3, 2)
  (1, 1) (2, 1) (3, 1)

The user places an 'X' not an 'O'
"""

cells = input("Enter cells: ")
print(f"""---------
| {cells[0]} {cells[1]} {cells[2]} |
| {cells[3]} {cells[4]} {cells[5]} |
| {cells[6]} {cells[7]} {cells[8]} |
--------- """)

b = [['-' for i in range(9)],
     ['_' for i in range(9)],
     ['_' for i in range(9)],
     ['_' for i in range(9)],
     ['-' for j in range(9)]
    ]

b[1][3] = cells[0]
b[2][3] = cells[1]
b[3][3] = cells[2]
b[1][2] = cells[3]
b[2][2] = cells[4]
b[3][2] = cells[5]
b[1][1] = cells[6]
b[2][1] = cells[7]
b[3][1] = cells[8]


while True:
    coord = input("Enter the coordinates: ")

    if coord.replace(" ", "").isnumeric() == False:
        print("You should enter numbers!")
    else:
        x, y = coord.split()
        if int(x) > 3 or int(y) > 3:
            print("Coordinates should be from 1 to 3!")
        else:
            x_coord = int(x)
            y_coord = int(y)

            if b[x_coord][y_coord] != '_':
                print("This cell is occupied! Choose another one!")
            else:
                b[x_coord][y_coord] = 'X'
                break

print(f"""---------
| {b[1][3]} {b[2][3]} {b[3][3]} |
| {b[1][2]} {b[2][2]} {b[3][2]} |
| {b[1][1]} {b[2][1]} {b[3][1]} |
--------- """)
