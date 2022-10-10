class anotherCharacterError(Exception):
    """Raised when user gives a character different from "x" or "o" or index out of an array"""
    pass


class occupiedField(Exception):
    """Raised when user tries to input a symbol to the index occupied by another symbol"""
    pass


def ifWin(sym):
    if ((fields[0] == sym and fields[1] == sym and fields[2] == sym)
            or (fields[3] == sym and fields[4] == sym and fields[5] == sym)
            or (fields[6] == sym and fields[7] == sym and fields[8] == sym)
            or (fields[0] == sym and fields[4] == sym and fields[8] == sym)
            or (fields[2] == sym and fields[4] == sym and fields[6] == sym)
            or (fields[0] == sym and fields[3] == sym and fields[6] == sym)
            or (fields[1] == sym and fields[4] == sym and fields[7] == sym)
            or (fields[2] == sym and fields[5] == sym and fields[8] == sym)):
        return True
    else:
        return False


def move(sym):
    while True:
        try:
            m = int(input("Insert an index of a field: "))

            # while m is not in the range of the table
            if m < 0 or m > 8:
                raise anotherCharacterError
            if fields[m] != " ":
                raise occupiedField

            # popping " " from the table
            fields.pop(m)
            # adding a symbol to the table
            fields.insert(m, sym)
            printingTable()

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


def printingTable():
    print(fields[0:3])
    print(fields[3:6])
    print(fields[6:9])


def oneRound():
    print(f"Player {1}")
    move("x")
    if ifWin("x"):
        return

    print(f"Player {2}")
    move("o")
    if ifWin("o"):
        return


def game():
    while ifWin("x") is not True and ifWin("o") is not True:
        oneRound()
    if ifWin("x"):
        return "Player 1 win."
    if ifWin("o"):
        return "Player 2 win."


fields = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

if __name__ == '__main__':
    print(game())
