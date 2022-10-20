class anotherCharacterError(Exception):
    """Raised when user gives a character different from "x" or "o" or index out of an array"""
    pass


class occupiedField(Exception):
    """Raised when user tries to input a symbol to the index occupied by another symbol"""
    pass


class game:
    # creating a game table
    def __init__(self):
        self.fields = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    # player choosing single-player or multiplayer mode
    def single_multi(self, ):


    # checking if a player made a move and win
    def ifWin(self, sym):
        if ((self.fields[0] == sym and self.fields[1] == sym and self.fields[2] == sym)
                or (self.fields[3] == sym and self.fields[4] == sym and self.fields[5] == sym)
                or (self.fields[6] == sym and self.fields[7] == sym and self.fields[8] == sym)
                or (self.fields[0] == sym and self.fields[4] == sym and self.fields[8] == sym)
                or (self.fields[2] == sym and self.fields[4] == sym and self.fields[6] == sym)
                or (self.fields[0] == sym and self.fields[3] == sym and self.fields[6] == sym)
                or (self.fields[1] == sym and self.fields[4] == sym and self.fields[7] == sym)
                or (self.fields[2] == sym and self.fields[5] == sym and self.fields[8] == sym)):
            return True
        else:
            return False

    # function for one signle move
    def move(self, sym):
        while True:
            try:
                m = int(input("Insert an index of a field: "))

                # while m is not in the range of the table
                if m < 0 or m > 8:
                    raise anotherCharacterError
                if self.fields[m] != " ":
                    raise occupiedField

                # popping " " from the table
                self.fields.pop(m)
                # adding a symbol to the table
                self.fields.insert(m, sym)
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
        print(self.fields[0:3])
        print(self.fields[3:6])
        print(self.fields[6:9])

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
