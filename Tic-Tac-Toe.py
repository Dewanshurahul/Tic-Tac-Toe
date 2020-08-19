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
            if board['7'] == board['8'] == board['9'] != ' ':  # across the top
                player_win_statement(7)
                break
            elif board['4'] == board['5'] == board['6'] != ' ':  # across the middle
                player_win_statement(4)
                break
            elif board['1'] == board['2'] == board['3'] != ' ':  # across the bottom
                player_win_statement(1)
                break
            elif board['1'] == board['4'] == board['7'] != ' ':  # down the left side
                player_win_statement(1)
                break
            elif board['2'] == board['5'] == board['8'] != ' ':  # down the middle
                player_win_statement(2)
                break
            elif board['3'] == board['6'] == board['9'] != ' ':  # down the right side
                player_win_statement(3)
                break
            elif board['7'] == board['5'] == board['3'] != ' ':  # diagonal
                player_win_statement(7)
                break
            elif board['1'] == board['5'] == board['9'] != ' ':  # diagonal
                player_win_statement(1)
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
            if board['7'] == board['8'] == board['9'] != ' ':  # across the top
                player_win_statement(7)
                break
            elif board['4'] == board['5'] == board['6'] != ' ':  # across the middle
                player_win_statement(4)
                break
            elif board['1'] == board['2'] == board['3'] != ' ':  # across the bottom
                player_win_statement(1)
                break
            elif board['1'] == board['4'] == board['7'] != ' ':  # down the left side
                player_win_statement(1)
                break
            elif board['2'] == board['5'] == board['8'] != ' ':  # down the middle
                player_win_statement(2)
                break
            elif board['3'] == board['6'] == board['9'] != ' ':  # down the right side
                player_win_statement(3)
                break
            elif board['7'] == board['5'] == board['3'] != ' ':  # diagonal
                player_win_statement(7)
                break
            elif board['1'] == board['5'] == board['9'] != ' ':  # diagonal
                player_win_statement(1)
                break

            count += 1
            toss = 0
        except:
            print("Error In Checking Game Status for Computer")
