# ----- Global Variables ----
# board
board = []
#  tell us if game is still going
game_still_going = True
# Who won? Or tie?
winner = None
# Whose turn is it
current_player = "X"
# create board


def create_board(l):
    for x in range(9):
        l.append('-')
    return l


create_board(board)


# display board


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# play game


def play_game():
    # Display initial board
    display_board()

    while game_still_going:
        # Handle_turn
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # flip players
        flip_player()


    # The game has ended
    if winner == 'X' or winner == 'O':
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# Handle a single turn for an arbitrary player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose  position from 1-9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9:")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there. Go again!")

    board[position] = player

    display_board()

# check if game is over


def check_if_game_over():
    check_for_winner()
    check_if_tie()


# check win


def check_for_winner():

    # Set up a global variable
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return


def check_rows():
    # Set up global variables
    global game_still_going
    # check if any of the rows have all the same value and is not empty
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    # If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # Set up global variables
    global game_still_going
    # check if any of the rows have all the same value and is not empty
    col_1 = board[0] == board[3] == board[6] != '-'
    col_2 = board[1] == board[4] == board[7] != '-'
    col_3 = board[2] == board[5] == board[8] != '-'
    # If any row does have a match, flag that there is a win
    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]
    return


def check_diagonals():
    # Set up global variables
    global game_still_going
    # check if any of the rows have all the same value and is not empty
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[6] == board[4] == board[2] != '-'
    # If any row does have a match, flag that there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

# check tie


def check_if_tie():
    # Set up a global variables
    global game_still_going

    if "-" not in board:
        game_still_going = False
    return


# flip player


def flip_player():
    # Set up a global variables
    global current_player
    # if the current player was x, then change it to O
    if current_player == "X":
        current_player = "O"
    # if the current player was 0 then change it to X
    elif current_player == "O":
        current_player = "X"

    return


# Run game
play_game()
