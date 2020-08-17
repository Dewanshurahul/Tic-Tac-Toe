from random import randint

print("Fresh start the Game.")
letter = ['O', 'X']
computer_letter = ''
player_letter = letter[randint(0, 1)]  # Randomly Assigning Letter to Player
if player_letter == 'X':
    computer_letter = 'O'
else:
    computer_letter = 'X'
print("Player got", player_letter, "letter")
print("Computer got", computer_letter, "letter")
toss = randint(0, 1)
count = 0  # To count number of Turns
if toss == 0:
    print("Player gets to Play")
else:
    print("Computer gets to Play")
# Creating board
board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}


# Printing Board
def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


corner = [1, 3, 7, 9]
move = 0
while True:
    # ------  Player Chance -----
    if toss == 0:
        print("Current Board is :")
        printboard(board)
        print("Player's Chance", player_letter)

        # Checking if Player Wins with the Move
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
        else:
            print("No Winning Condition")

        # Checking if Computer(Opponent) Wins with the Move
        if move == 0:
            if (board['1'] == computer_letter and board['2'] == computer_letter and board['3'] == " ") or (
                    board['1'] == computer_letter and board['2'] == " " and board['3'] == computer_letter) or (
                    board['1'] == " " and board['2'] == computer_letter and board['3'] == computer_letter):
                if board['1'] == " ":
                    move = 1
                elif board['2'] == " ":
                    move = 2
                else:
                    move = 3
            elif (board['4'] == computer_letter and board['5'] == computer_letter and board['6'] == " ") or (
                    board['4'] == computer_letter and board['5'] == " " and board['6'] == computer_letter) or (
                    board['4'] == " " and board['5'] == computer_letter and board['6'] == computer_letter):
                if board['4'] == " ":
                    move = 4
                elif board['5'] == " ":
                    move = 5
                else:
                    move = 6
            elif (board['7'] == computer_letter and board['8'] == computer_letter and board['9'] == " ") or (
                    board['7'] == computer_letter and board['8'] == " " and board['9'] == computer_letter) or (
                    board['7'] == " " and board['8'] == computer_letter and board['9'] == computer_letter):
                if board['7'] == " ":
                    move = 7
                elif board['8'] == " ":
                    move = 8
                else:
                    move = 9
            elif (board['1'] == computer_letter and board['4'] == computer_letter and board['7'] == " ") or (
                    board['1'] == computer_letter and board['4'] == " " and board['7'] == computer_letter) or (
                    board['1'] == " " and board['4'] == computer_letter and board['7'] == computer_letter):
                if board['1'] == " ":
                    move = 1
                elif board['4'] == " ":
                    move = 4
                else:
                    move = 7
            elif (board['2'] == computer_letter and board['5'] == computer_letter and board['8'] == " ") or (
                    board['2'] == computer_letter and board['5'] == " " and board['8'] == computer_letter) or (
                    board['2'] == " " and board['5'] == computer_letter and board['8'] == computer_letter):
                if board['2'] == " ":
                    move = 2
                elif board['5'] == " ":
                    move = 5
                else:
                    move = 8
            elif (board['3'] == computer_letter and board['6'] == computer_letter and board['9'] == " ") or (
                    board['3'] == computer_letter and board['6'] == " " and board['9'] == computer_letter) or (
                    board['3'] == " " and board['6'] == computer_letter and board['9'] == computer_letter):
                if board['3'] == " ":
                    move = 3
                elif board['6'] == " ":
                    move = 6
                else:
                    move = 9
            elif (board['1'] == computer_letter and board['5'] == computer_letter and board['9'] == " ") or (
                    board['1'] == computer_letter and board['5'] == " " and board['9'] == computer_letter) or (
                    board['1'] == " " and board['5'] == computer_letter and board['9'] == computer_letter):
                if board['1'] == " ":
                    move = 1
                elif board['5'] == " ":
                    move = 5
                else:
                    move = 9
            elif (board['3'] == computer_letter and board['5'] == computer_letter and board['7'] == " ") or (
                    board['3'] == computer_letter and board['5'] == " " and board['7'] == computer_letter) or (
                    board['3'] == " " and board['5'] == computer_letter and board['7'] == computer_letter):
                if board['3'] == " ":
                    move = 3
                elif board['5'] == " ":
                    move = 5
                else:
                    move = 7

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

        if board[str(move)] != " ":
            print("Position already Occupied")
            continue
        else:
            board[str(move)] = player_letter

        # Checking for Game Status (Winner/Loss/Tie)
        if board['7'] == board['8'] == board['9'] != ' ':  # across the top
            if player_letter == board['7']:
                print("Player Wins")
            else:
                print("Computer Wins")
            break
        elif board['4'] == board['5'] == board['6'] != ' ':  # across the middle
            if player_letter == board['4']:
                print("Player Wins")
            else:
                print("Computer Wins")
            break
        elif board['1'] == board['2'] == board['3'] != ' ':  # across the bottom
            if player_letter == board['1']:
                print("Player Wins")
            else:
                print("Computer Wins")
            break
        elif board['1'] == board['4'] == board['7'] != ' ':  # down the left side
            if player_letter == board['1']:
                print("Player Wins")
            else:
                print("Computer Wins")
            break
        elif board['2'] == board['5'] == board['8'] != ' ':  # down the middle
            if player_letter == board['2']:
                print("Player Wins")
            else:
                print("Computer Wins")
            break
        elif board['3'] == board['6'] == board['9'] != ' ':  # down the right side
            if player_letter == board['3']:
                print("Player Wins")
            else:
                print("Computer Wins")
            break
        elif board['7'] == board['5'] == board['3'] != ' ':  # diagonal
            if player_letter == board['7']:
                print("Player Wins")
            else:
                print("Computer Wins")
            break
        elif board['1'] == board['5'] == board['9'] != ' ':  # diagonal
            if player_letter == board['1']:
                print("Player Wins")
            else:
                print("Computer Wins")
            break

        if count == 9:
            print("Game Ties.")
        count += 1
        toss = 1
        continue

    else:
        # ----- Computer Chance -----
        print("Current Board is :")
        printboard(board)
        print("Computer's Chance", computer_letter)
        move = 0

        # Checking if Computer Wins with the Move
        if (board['1'] == computer_letter and board['2'] == computer_letter and board['3'] == " ") or (
                board['1'] == computer_letter and board['2'] == " " and board['3'] == computer_letter) or (
                board['1'] == " " and board['2'] == computer_letter and board['3'] == computer_letter):
            if board['1'] == " ":
                move = 1
            elif board['2'] == " ":
                move = 2
            else:
                move = 3
        elif (board['4'] == computer_letter and board['5'] == computer_letter and board['6'] == " ") or (
                board['4'] == computer_letter and board['5'] == " " and board['6'] == computer_letter) or (
                board['4'] == " " and board['5'] == computer_letter and board['6'] == computer_letter):
            if board['4'] == " ":
                move = 4
            elif board['5'] == " ":
                move = 5
            else:
                move = 6
        elif (board['7'] == computer_letter and board['8'] == computer_letter and board['9'] == " ") or (
                board['7'] == computer_letter and board['8'] == " " and board['9'] == computer_letter) or (
                board['7'] == " " and board['8'] == computer_letter and board['9'] == computer_letter):
            if board['7'] == " ":
                move = 7
            elif board['8'] == " ":
                move = 8
            else:
                move = 9
        elif (board['1'] == computer_letter and board['4'] == computer_letter and board['7'] == " ") or (
                board['1'] == computer_letter and board['4'] == " " and board['7'] == computer_letter) or (
                board['1'] == " " and board['4'] == computer_letter and board['7'] == computer_letter):
            if board['1'] == " ":
                move = 1
            elif board['4'] == " ":
                move = 4
            else:
                move = 7
        elif (board['2'] == computer_letter and board['5'] == computer_letter and board['8'] == " ") or (
                board['2'] == computer_letter and board['5'] == " " and board['8'] == computer_letter) or (
                board['2'] == " " and board['5'] == computer_letter and board['8'] == computer_letter):
            if board['2'] == " ":
                move = 2
            elif board['5'] == " ":
                move = 5
            else:
                move = 8
        elif (board['3'] == computer_letter and board['6'] == computer_letter and board['9'] == " ") or (
                board['3'] == computer_letter and board['6'] == " " and board['9'] == computer_letter) or (
                board['3'] == " " and board['6'] == computer_letter and board['9'] == computer_letter):
            if board['3'] == " ":
                move = 3
            elif board['6'] == " ":
                move = 6
            else:
                move = 9
        elif (board['1'] == computer_letter and board['5'] == computer_letter and board['9'] == " ") or (
                board['1'] == computer_letter and board['5'] == " " and board['9'] == computer_letter) or (
                board['1'] == " " and board['5'] == computer_letter and board['9'] == computer_letter):
            if board['1'] == " ":
                move = 1
            elif board['5'] == " ":
                move = 5
            else:
                move = 9
        elif (board['3'] == computer_letter and board['5'] == computer_letter and board['7'] == " ") or (
                board['3'] == computer_letter and board['5'] == " " and board['7'] == computer_letter) or (
                board['3'] == " " and board['5'] == computer_letter and board['7'] == computer_letter):
            if board['3'] == " ":
                move = 3
            elif board['5'] == " ":
                move = 5
            else:
                move = 7
        else:
            print("No Winning Condition")

        # Checking if Player(Opponent) Wins with the Move
        if move == 0:
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

        if board[str(move)] != " ":
            print("Position already Occupied")
            continue
        else:
            board[str(move)] = computer_letter

        # Checking for Game Status (Winner/Loss/Tie)
        if board['7'] == board['8'] == board['9'] != ' ':  # across the top
            if computer_letter == board['7']:
                print("Computer Wins")
            else:
                print("Player Wins")
            break
        elif board['4'] == board['5'] == board['6'] != ' ':  # across the middle
            if computer_letter == board['4']:
                print("Computer Wins")
            else:
                print("Player Wins")
            break
        elif board['1'] == board['2'] == board['3'] != ' ':  # across the bottom
            if computer_letter == board['1']:
                print("Computer Wins")
            else:
                print("Player Wins")
            break
        elif board['1'] == board['4'] == board['7'] != ' ':  # down the left side
            if computer_letter == board['1']:
                print("Computer Wins")
            else:
                print("Player Wins")
            break
        elif board['2'] == board['5'] == board['8'] != ' ':  # down the middle
            if computer_letter == board['2']:
                print("Computer Wins")
            else:
                print("Player Wins")
            break
        elif board['3'] == board['6'] == board['9'] != ' ':  # down the right side
            if computer_letter == board['3']:
                print("Computer Wins")
            else:
                print("Player Wins")
            break
        elif board['7'] == board['5'] == board['3'] != ' ':  # diagonal
            if computer_letter == board['7']:
                print("Computer Wins")
            else:
                print("Player Wins")
            break
        elif board['1'] == board['5'] == board['9'] != ' ':  # diagonal
            if computer_letter == board['1']:
                print("Computer Wins")
            else:
                print("Player Wins")
            break

        if count == 9:
            print("Game Ties.")
            break
        count += 1
        toss = 0
