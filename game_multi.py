class anotherCharacterError(Exception):
    """Raised when user gives a character different from "x" or "o" or index out of an array"""
    pass


class occupiedField(Exception):
    """Raised when user tries to input a symbol to the index occupied by another symbol"""
    pass


class game_multi:
    # creating a game table
    def __init__(self):
        self.fields = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    # checking if a player made a move and win
    def ifWin(self, sym):
        if ((self.fields[0][0] == sym and self.fields[0][1] == sym and self.fields[0][2] == sym)
                or (self.fields[1][0] == sym and self.fields[1][1] == sym and self.fields[1][2] == sym)
                or (self.fields[2][0] == sym and self.fields[2][1] == sym and self.fields[2][2] == sym)
                or (self.fields[0][0] == sym and self.fields[1][1] == sym and self.fields[2][2] == sym)
                or (self.fields[0][2] == sym and self.fields[1][1] == sym and self.fields[2][0] == sym)
                or (self.fields[0][0] == sym and self.fields[1][0] == sym and self.fields[2][0] == sym)
                or (self.fields[0][1] == sym and self.fields[1][1] == sym and self.fields[2][1] == sym)
                or (self.fields[0][2] == sym and self.fields[1][2] == sym and self.fields[2][2] == sym)):
            return True
        else:
            return False

    # function for one signle move
    def move(self, sym):
        while True:
            try:
                m = int(input("Insert an index of a column: "))
                n = int(input("Insert an index of a row: "))

                # while m is not in the range of the table
                if m < 0 or m > 2 or n < 0 or n > 2:
                    raise anotherCharacterError
                if self.fields[n][m] != ' ':
                    raise occupiedField

                self.fields[n][m] = sym
                self.printingTable()

            except ValueError:
                print("Incorrect sign.")
                continue
            except anotherCharacterError:
                print("Index outside of an array.")
                continue
            except occupiedField:
                print("Field occupied.")
                continue
            break

    def printingTable(self):
        print(self.fields[0][0:3])
        print(self.fields[1][0:3])
        print(self.fields[2][0:3])

    def oneRound(self):
        print(f"Player {1}")
        self.move("x")
        if self.ifWin("x"):
            return

        print(f"Player {2}")
        self.move("o")
        if self.ifWin("o"):
            return

    def play(self):
        while self.ifWin("x") is not True and self.ifWin("o") is not True:
            self.oneRound()
        if self.ifWin("x"):
            return "Player 1 win."
        if self.ifWin("o"):
            return "Player 2 win."
