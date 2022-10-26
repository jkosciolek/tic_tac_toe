from game_multi import game_multi

"""
I'm using minimax algorithm to define computer moves in a singleplayer mode. This algorithm is minimizing the possible 
loss, so it's unbeatable. I can implement a weaker opponent that is making decisions by random.

X - maximising player
O - minimising player
"""


class game_single(game_multi):
    def __init__(self):
        super().__init__()
        self.fields = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


    def AI_move(self):
        best_score = float('-inf')

