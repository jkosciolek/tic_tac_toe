from game_multi import game_multi


class anotherCharacterError(Exception):
    """Raised when user gives a different input from 'single' or 'multi' """
    pass


if __name__ == '__main__':
    print("Welcome in Tic Tac Toe!")
    while True:
        try:
            mode = input("Please type 'single' if you want to play in a singleplayer mode"
                         "or 'multi' if you want to play in a multiplayer mode: ")
            if mode == 'multi':
                game1 = game_multi()
                print(game1.play())
            # elif mode == 'single':
            #     game1 = game_single()
            #     print(game1.play())
            else:
                raise anotherCharacterError
        except anotherCharacterError:
            continue
        break
