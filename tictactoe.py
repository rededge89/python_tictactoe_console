import math

game_continue = True


def check_row(board):
    x = 0
    o = 0
    for i in range(3):
        if board[i].count("X") == 3:
            x += 1
        elif board[i].count("O") == 3:
            o += 1
    return [x, o]


def check_vertical(board):
    x = 0
    o = 0
    for i in range(0, 3):
        check_list = [board[0][i], board[1][i], board[2][i]]
        if check_list.count("X") == 3:
            x += 1
        elif check_list.count("O") == 3:
            o += 1
    return [x, o]


def check_diagonal(board):
    x = 0
    o = 0
    check_list = []
    check_list2 = []
    for j in range(3):
        check_list.append(board[j][j])
        check_list2.append(board[j][int(math.fabs(j - 2))])
    if check_list.count("X") == 3 or check_list2.count("X") == 3:
        x += 1
    elif check_list.count("O") == 3 or check_list2.count("O") == 3:
        o += 1
    return [x, o]


def impossible_check(win_tracker_list, all_inputs):
    x_wins = 0
    o_wins = 0
    for i in range(len(win_tracker_list)):
        if i % 2 == 0:
            x_wins += win_tracker_list[i]
        elif i % 2 == 1:
            o_wins += win_tracker_list[i]
    if x_wins > 0 and o_wins > 0 or x_wins > 1 or o_wins > 1:
        print("Impossible")
        return False
    elif all_inputs.count("X") >= all_inputs.count("O") + 2 or all_inputs.count("O") >= all_inputs.count("X") + 2:
        print("Impossible")
        return False
    else:
        return True


def draw_finish_check(board):
    i = 0
    for k in range(3):
        for l in range (3):
            if board[k][l] == "_":
                i += 1
    if i == 0:
        global game_continue
        game_continue = False
        print("Draw")


def win_check(win_tracker_list):
    global game_continue
    for i in range(len(win_tracker_list)):
        if i % 2 == 0:
            if win_tracker_list[i] == 1:
                print("X wins")
                game_continue = False
                return False
        elif i % 2 == 1:
            if win_tracker_list[i] == 1:
                print("O wins")
                game_continue = False
                return False
    return True


# program start
XO_user_input = "_ _ _ _ _ _ _ _ _"
XO_user_input = XO_user_input.split()
matrix = []
win_tracker = []
game_continue = True
# loop to create a matrix
for i in range(0, len(XO_user_input), 3):
    j = i + 3
    matrix.append(XO_user_input[i:j])
# print TTT board
print("---------")
print(f'| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |')
print(f'| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |')
print(f'| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |')
print("---------")
pawn = "O"
while game_continue:
    if pawn == "O":
        pawn = "X"
    elif pawn == "X":
        pawn = "O"
    coordinate_loop = True
    while coordinate_loop:
        try:
            coordinate = input("Enter the coordinate: ")
            cord_list = coordinate.split()
            coordinate_x = int(cord_list[0])
            coordinate_y = int(cord_list[1])
            for number in cord_list:
                if int(number) > 3 or int(number) < 1:
                    print("Coordinates should be from 1 to 3!")
                    break
                elif matrix[int(math.fabs(coordinate_y - 3))][coordinate_x - 1] != "_":
                    print("This cell is occupied! Choose another one!")
                    break
                else:
                    coordinate_loop = False
        except ValueError:
            print("You should enter numbers!")
        except IndexError:
            print("You must enter an X and Y coordinate!")
    matrix[int(math.fabs(coordinate_y - 3))][coordinate_x - 1] = pawn
    print("---------")
    print(f'| {matrix[0][0]} {matrix[0][1]} {matrix[0][2]} |')
    print(f'| {matrix[1][0]} {matrix[1][1]} {matrix[1][2]} |')
    print(f'| {matrix[2][0]} {matrix[2][1]} {matrix[2][2]} |')
    print("---------")
    win_tracker.extend(check_row(matrix))
    win_tracker.extend(check_vertical(matrix))
    win_tracker.extend(check_diagonal(matrix))
    if impossible_check(win_tracker, XO_user_input):
        if win_check(win_tracker):
            draw_finish_check(matrix)
