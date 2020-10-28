# Project Tic Tac Toe


# --------------------- Global Variables-----------------------------
# Board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

game_still_going = True

winner = None

current_player = "X"

#Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    # Initial board
    display_board()

    while game_still_going:
        handle_turn(current_player)

        check_if_game_over()

        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " Won")
    elif winner == None:
        print("Tie")

    terminate = input("Press any key to exit")

def handle_turn(player):
    print(player + "'s turn")

    position = input("Enter the position from 1-9")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Enter valid input i.e from 1-9")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("It's already occupied... Enter the position once again")

    board[position] = player
    display_board()


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


def check_if_game_over():
    check_if_win()
    check_if_tie()

def check_if_win():
    global winner

    column_winner = check_column()
    row_winner = check_row()
    diagonal_winner = check_diagonal()

    if column_winner:
        winner = column_winner
    elif row_winner:
        winner = row_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False
    return

def check_row():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:
        game_still_going = False

    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_column():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:
        game_still_going = False

    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonal():
    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

play_game()