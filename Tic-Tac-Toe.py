from random import randint

print("Fresh start the Game.")
letter = ['O', 'X']
computer_letter = ''
def player_letter_assignment(letter):
    return letter[randint(0, 1)]
player_letter = player_letter_assignment(letter)  # Randomly Assigning Letter to Player
def computer_letter_assignment(player_letter):
    if player_letter == 'X':
        return 'O'
    return 'X'
computer_letter = computer_letter_assignment(player_letter)
toss = randint(0, 1)
count = 0  # To count number of Turns
# Creating board
board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}

move = 0

def validate_input(input):
    if input in str([1,2,3,4,5,6,7,8,9]):
        return True
    return False


def status_horizontal():
    for position in range(1, 8, 3):
        if board[str(position)] == board[str(position + 1)] == board[str(position + 2)] != ' ':  # across the top
            return position
    return 0

def status_vertical():
    for position in range(1, 4):
        if board[str(position)] == board[str(position + 3)] == board[str(position + 6)] != ' ':  # across the top
            return position
    return 0


def status_diagonal_left():
    if board[str(1)] == board[str(5)] == board[str(9)] != ' ':  # across the top
            return 1
    return 0


def status_diagonal_right():
    if board[str(3)] == board[str(5)] == board[str(7)] != ' ':  # across the top
        return 3
    return 0


def player_win_move_vertical(player_letter):
    for position in range(1, 4):
        if (board[str(position)] == player_letter and board[str(position + 3)] == player_letter and board[str(position + 6)] == " ") or (
                board[str(position)] == player_letter and board[str(position + 3)] == " " and board[str(position + 6)] == player_letter) or (
                board[str(position)] == player_letter and board[str(position + 3)] == player_letter and board[str(position + 6)] == " "):
            for horizontal_position in range(position, position + 7, 3):
                if board[str(horizontal_position)] == " ":
                    return horizontal_position
    return 0


def player_win_move_horizontal(player_letter):
    for position in range(1, 8, 3):
        if (board[str(position)] == player_letter and board[str(position + 1)] == player_letter and board[str(position + 2)] == " ") or (
                board[str(position)] == player_letter and board[str(position + 1)] == " " and board[str(position + 2)] == player_letter) or (
                board[str(position)] == player_letter and board[str(position + 1)] == player_letter and board[str(position + 2)] == " "):
            for horizontal_position in range(position, position + 3):
                if board[str(horizontal_position)] == " ":
                    return horizontal_position
    return 0


def player_win_move_diagonal(player_letter):
    if (board['1'] == player_letter and board['5'] == player_letter and board['9'] == " ") or (
            board['1'] == player_letter and board['5'] == " " and board['9'] == player_letter) or (
            board['1'] == " " and board['5'] == player_letter and board['9'] == player_letter):
        if board['1'] == " ":
            move = 1
        elif board['5'] == " ":
            move = 5
        else:
            move = 9
    elif (board['3'] == player_letter and board['5'] == player_letter and board['7'] == " ") or (
            board['3'] == player_letter and board['5'] == " " and board['7'] == player_letter) or (
            board['3'] == " " and board['5'] == player_letter and board['7'] == player_letter):
        if board['3'] == " ":
            move = 3
        elif board['5'] == " ":
            move = 5
        else:
            move = 7
    return move


def player_win_statement(pindex):
    if player_letter == board[str(pindex)]:
        print("Player Wins")
    else:
        print("Computer Wins")


# Printing Board
def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


while True:
    # ------  Player Chance -----
    if toss == 0:
        if count == 9:
            print("Game Ties.")
            break
        move = 0
        print("Current Board is :")
        try:
            printboard(board)
        except:
            print("Error in Printing Player Board")

        move = input("Enter the Position 1 - 9 : ")

        if validate_input(move) and board[str(move)] == " ":
            board[str(move)] = player_letter
        else:
            continue

        # Checking for Game Status (Winner/Loss/Tie)
        try:
            if status_horizontal() != 0:
                player_win_statement(str(status_horizontal()))
                break
            elif status_vertical() != 0:
                player_win_statement(str(status_vertical()))
                break
            elif status_diagonal_left() != 0:
                player_win_statement(str(status_diagonal_left()))
                break
            elif status_diagonal_right() != 0:
                player_win_statement(str(status_diagonal_right()))
                break
            count += 1
            toss = 1
            continue
        except:
            print("Error in Checking Game Status for Player")
    else:
        # ----- Computer Chance -----
        if count == 9:
            print("Game Ties.")
            break
        try:
            printboard(board)
        except:
            print("Board is Not Printed")
        move = 0

        # Checking if Computer Wins with the Move
        try:
            if player_win_move_horizontal(computer_letter) != 0:
                move = player_win_move_horizontal(computer_letter)
            elif player_win_move_vertical(computer_letter) != 0:
                move = player_win_move_vertical(computer_letter)
            elif player_win_move_diagonal(computer_letter) != 0:
                move = player_win_move_diagonal(computer_letter)
        except:
            print("Error in Checking Computer Winning Move")

        # Checking if Player(Opponent) Wins with the Move
        try:
            if move == 0:
                if player_win_move_horizontal(player_letter) != 0:
                    move = player_win_move_horizontal(player_letter)
                elif player_win_move_vertical(player_letter) != 0:
                    move = player_win_move_vertical(player_letter)
                elif player_win_move_diagonal(player_letter) != 0:
                    move = player_win_move_diagonal(player_letter)
        except:
            print("Error in Checking Player (Opponent) Winning Move")

        # Corner Choice
        if move == 0:
            if board['1'] == ' ':
                move = 1
            elif board['3'] == ' ':
                move = 3
            elif board['7'] == ' ':
                move = 7
            elif board['9'] == ' ':
                move = 9
            elif board['5'] == " ":  # middle Choice for player (Use Case_10)
                move =5
        # Side Place Choice
            elif board['4'] == ' ':
                move = 4
            elif board['2'] == ' ':
                move = 2
            elif board['6'] == ' ':
                move = 6
            elif board['8'] == ' ':
                move = 8

        if board[str(move)] == " ":
            board[str(move)] = computer_letter
        else:
            continue

        # Checking for Game Status (Winner/Loss/Tie)
        try:
            if status_horizontal() != 0:
                player_win_statement(str(status_horizontal()))
                break
            elif status_vertical() != 0:
                player_win_statement(str(status_vertical()))
                break
            elif status_diagonal_left() != 0:
                player_win_statement(str(status_diagonal_left()))
                break
            elif status_diagonal_right() != 0:
                player_win_statement(str(status_diagonal_right()))
                break

            count += 1
            toss = 0
        except:
            print("Error In Checking Game Status for Computer")
