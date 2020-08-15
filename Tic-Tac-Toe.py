from random import randint
print("Fresh start the Game.")
letter = ['O', 'X']
player_letter = letter[randint(0, 1)]
print("Player got", player_letter, "letter")
toss = randint(0, 1)
count = 0  # To count number of Turns
if toss == 0:
    print("Player gets to Play")
else:
    print("Computer gets to Play")

board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}


def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


print("Current Board is :")
printboard(board)


def gamestatus(board):
    if board['7'] == board['8'] == board['9'] != ' ':  # across the top
        if player_letter == board['7']:
            print("Player Wins")
        else:
            print("Computer Wins")
    elif board['4'] == board['5'] == board['6'] != ' ':  # across the middle
        if player_letter == board['4']:
            print("Player Wins")
        else:
            print("Computer Wins")
    elif board['1'] == board['2'] == board['3'] != ' ':  # across the bottom
        if player_letter == board['1']:
            print("Player Wins")
        else:
            print("Computer Wins")
    elif board['1'] == board['4'] == board['7'] != ' ':  # down the left side
        if player_letter == board['1']:
            print("Player Wins")
        else:
            print("Computer Wins")
    elif board['2'] == board['5'] == board['8'] != ' ':  # down the middle
        if player_letter == board['2']:
            print("Player Wins")
        else:
            print("Computer Wins")
    elif board['3'] == board['6'] == board['9'] != ' ':  # down the right side
        if player_letter == board['3']:
            print("Player Wins")
        else:
            print("Computer Wins")
    elif board['7'] == board['5'] == board['3'] != ' ':  # diagonal
        if player_letter == board['7']:
            print("Player Wins")
        else:
            print("Computer Wins")
    elif board['1'] == board['5'] == board['9'] != ' ':  # diagonal
        if player_letter == board['1']:
            print("Player Wins")
        else:
            print("Computer Wins")

    if count == 9:
        print("Game Ties.")


gamestatus(board)
