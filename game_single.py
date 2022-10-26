from game_multi import game_multi

"""
I'm using minimax algorithm to define computer moves in a singleplayer mode. This algorithm is minimizing the possible 
loss, so it's unbeatable. I can implement a weaker opponent that is making decisions by random.

X - maximising player, player
O - minimising player, AI 
"""


class game_single(game_multi):
    def __init__(self):
        super().__init__()
        self.fields = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def points(self):
        # points for rows victory
        for row in range(3):
            if self.fields[row][0] == self.fields[row][1] and self.fields[row][1] == self.fields[row][2]:
                if self.fields[row][0] == 'x':
                    return 10
                elif self.fields[row][0] == 'o':
                    return -10

        # points for columns victory
        for col in range(3):
            if self.fields[0][col] == self.fields[1][col] and self.fields[1][col] == self.fields[2][col]:
                if self.fields[0][col] == 'x':
                    return 10
                elif self.fields[0][col] == 'o':
                    return -10

        # points for diagonals victory
        if self.fields[0][0] == self.fields[1][1] and self.fields[1][1] == self.fields[2][2]:
            if self.fields[0][0] == 'x':
                return 10
            elif self.fields[0][0] == 'o':
                return -10

        if self.fields[0][2] == self.fields[1][1] and self.fields[1][1] == self.fields[2][0]:
            if self.fields[0][2] == 'x':
                return 10
            elif self.fields[0][2] == 'o':
                return -10

        # none of players won
        return 0
