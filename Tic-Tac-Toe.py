from random import randint
print("Fresh start the Game.")
letter = ['O', 'X']
player_letter = letter[randint(0, 1)]
print("Player got", player_letter, "letter")
toss = randint(0, 1)
if toss == 0:
    print("Player gets to Play")
else:
    print("Computer gets to Play")

board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
print("Current Board is :")
printBoard(board)