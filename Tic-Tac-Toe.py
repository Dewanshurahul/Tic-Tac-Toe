from random import randint

print("Fresh start the Game.")
letter = ['O', 'X']
computer_letter = ''
player_letter = letter[randint(0, 1)]  # Randomly Assigning Letter to Player
if player_letter == 'X':
    computer_letter = 'O'
else:
    computer_letter = 'X'
toss = randint(0, 1)
count = 0  # To count number of Turns
# Creating board
board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}

move = 0

def status_horizontal():
    for x in range(1, 8, 3):
        if board[str(x)] == board[str(x+1)] == board[str(x+2)] != ' ':  # across the top
            return x
    return 0

def status_vertical():
    for x in range(1, 4):
        if board[str(x)] == board[str(x+3)] == board[str(x+6)] != ' ':  # across the top
            return x
    return 0


def status_diagonal_left():
    if board[str(1)] == board[str(5)] == board[str(9)] != ' ':  # across the top
            return 1
    return 0


def status_diagonal_right():
    if board[str(3)] == board[str(5)] == board[str(7)] != ' ':  # across the top
        return 3
    return 0


def player_win_move(player_letter):
    if (board['1'] == player_letter and board['2'] == player_letter and board['3'] == " ") or (
            board['1'] == player_letter and board['2'] == " " and board['3'] == player_letter) or (
            board['1'] == " " and board['2'] == player_letter and board['3'] == player_letter):
        if board['1'] == " ":
            move = 1
        elif board['2'] == " ":
            move = 2
        else:
            move = 3
    elif (board['4'] == player_letter and board['5'] == player_letter and board['6'] == " ") or (
            board['4'] == player_letter and board['5'] == " " and board['6'] == player_letter) or (
            board['4'] == " " and board['5'] == player_letter and board['6'] == player_letter):
        if board['4'] == " ":
            move = 4
        elif board['5'] == " ":
            move = 5
        else:
            move = 6
    elif (board['7'] == player_letter and board['8'] == player_letter and board['9'] == " ") or (
            board['7'] == player_letter and board['8'] == " " and board['9'] == player_letter) or (
            board['7'] == " " and board['8'] == player_letter and board['9'] == player_letter):
        if board['7'] == " ":
            move = 7
        elif board['8'] == " ":
            move = 8
        else:
            move = 9
    elif (board['1'] == player_letter and board['4'] == player_letter and board['7'] == " ") or (
            board['1'] == player_letter and board['4'] == " " and board['7'] == player_letter) or (
            board['1'] == " " and board['4'] == player_letter and board['7'] == player_letter):
        if board['1'] == " ":
            move = 1
        elif board['4'] == " ":
            move = 4
        else:
            move = 7
    elif (board['2'] == player_letter and board['5'] == player_letter and board['8'] == " ") or (
            board['2'] == player_letter and board['5'] == " " and board['8'] == player_letter) or (
            board['2'] == " " and board['5'] == player_letter and board['8'] == player_letter):
        if board['2'] == " ":
            move = 2
        elif board['5'] == " ":
            move = 5
        else:
            move = 8
    elif (board['3'] == player_letter and board['6'] == player_letter and board['9'] == " ") or (
            board['3'] == player_letter and board['6'] == " " and board['9'] == player_letter) or (
            board['3'] == " " and board['6'] == player_letter and board['9'] == player_letter):
        if board['3'] == " ":
            move = 3
        elif board['6'] == " ":
            move = 6
        else:
            move = 9
    elif (board['1'] == player_letter and board['5'] == player_letter and board['9'] == " ") or (
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

        if board[str(move)] == " ":
            board[str(move)] = player_letter
        else:
            continue

        # Checking for Game Status (Winner/Loss/Tie)
        try:
            if status_horizontal() != 0:
                player_win_statement(str(status_horizontal()))
            elif status_vertical() != 0:
                player_win_statement(str(status_vertical()))
            elif status_diagonal_left() != 0:
                player_win_statement(str(status_diagonal_left()))
            elif status_diagonal_right() != 0:
                player_win_statement(str(status_diagonal_right()))
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
            move = player_win_move(computer_letter)
        except:
            print("Error in Checking Computer Winning Move")

        # Checking if Player(Opponent) Wins with the Move
        try:
            if move == 0:
                move = player_win_move(player_letter)
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
            else:
                print("0")

            count += 1
            toss = 0
        except:
            print("Error In Checking Game Status for Computer")
