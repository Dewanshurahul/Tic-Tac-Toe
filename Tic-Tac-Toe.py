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


while True:
    # ------  Player Chance -----
    if toss == 0:
        print("Current Board is :")
        printboard(board)
        print("Player's Chance", player_letter)
        move = input("Enter the Position 1 - 9 : ")
        if board[move] != " ":
            print("Position already Occupied")
            continue
        else:
            board[move] = player_letter
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
        move = input("Enter the Position 1 - 9 : ")
        if board[move] != " ":
            print("Position already Occupied")
            continue
        else:
            board[move] = computer_letter
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
