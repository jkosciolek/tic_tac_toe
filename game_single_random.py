from game_multi import game_multi
import random

"""
This is the easier version of singleplayer mode. Player's opponent is choosing a random field to place his symbol.

Player: "o"
Opponent: "x"
"""


class game_single_random(game_multi):
    def __init__(self):
        super().__init__()
        self.fields = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def oneRound(self):
        # player
        if self.isMoveAvailable():
            print(f"\nPlayer {1}")
            self.move("o")
            if self.ifWin("o"):
                return
        else:
            return

        # opponent
        if self.isMoveAvailable():

            print(f"\nPlayer{2}")
            # guessing random field
            a, b = random.randint(0,2), random.randint(0, 2)

            # if this field is occupied, try another field
            while self.fields[a][b] != ' ':
                a, b = random.randint(0, 2), random.randint(0, 2)

            self.fields[a][b] = "x"
            self.printingTable()

            if self.ifWin("x"):
                return
        else:
            return

