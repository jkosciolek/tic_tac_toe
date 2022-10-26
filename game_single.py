from game_multi import game_multi
import numpy as np

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

    def possibleMoves(self):
        moves = []
        for row in range(3):
            for column in range(3):
                if self.fields[row][column] == ' ':
                    moves.append(self.fields[row][column])
        return moves

    # finding the best possible move for the player
    def bestMove(self):
        bestScore = -np.inf
        bestMove = (-1, -1)

        for row in range(3):
            for column in range(3):

                if self.fields[row][column] == ' ':
                    self.fields[row][column] = 'o'
                    moveScore = self.minimax(0, False)

                    # undo the move
                    self.fields[row][column] == ' '

                    if moveScore > bestScore:
                        bestMove = (row, column)
                        bestScore = moveScore
        print(f"The value of the best move is: {bestScore}")
        return bestMove

    def minimax(self, depth, isMax):
        score = self.points()

        # maximizer == 10, minimizer == -10 won the game
        if score == 10 or score == -10:
            return score

        # tie
        if not self.isMoveAvailable():
            return 0

        # minimizer - computer move
        best = 1000

        for row in range(3):
            for column in range(3):
                if self.fields[row][column] == ' ':
                    self.fields[row][column] = 'o'

                    # call minimax recursively and choose the minimum value
                    best = min(best, self.minimax(depth + 1, not isMax))

                    # undo the move
                    self.fields[row][column] = ' '
        return best

    def oneRound(self):
        if self.isMoveAvailable():
            print(f"Player {1}")
            self.move("x")
            if self.ifWin("x"):
                return
        else:
            return

        if self.isMoveAvailable():
            print(f"Player {2}")
            self.aiMove()
            if self.ifWin("o"):
                return
        else:
            return

    def aiMove(self):
        bestMove = self.bestMove()
        print("The optimal move is: ")
        print(f"ROW: {bestMove[0]} COL: {bestMove[1]}")
        self.fields[bestMove[0]][bestMove[1]]
