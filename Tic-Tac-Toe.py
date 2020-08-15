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
