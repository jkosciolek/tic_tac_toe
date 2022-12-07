from game_multi import game_multi
from game_single_random import game_single_random
from app import App


class anotherCharacterError(Exception):
    """Raised when user gives a different input from 'single' or 'multi' """
    pass


if __name__ == '__main__':
    print("Welcome in Tic Tac Toe!")
    playing = "yes"
    while playing == "yes":

        while True:
            app = App()
            app.mainloop()
            try:
                mode = input("\n\nPlease type 'single' if you want to play in a singleplayer mode"
                             " or 'multi' if you want to play in a multiplayer mode: ")
                if mode == 'multi':
                    game1 = game_multi()
                    print(game1.play())
                elif mode == 'single':
                    game1 = game_single_random()
                    print(game1.play())
                else:
                    raise anotherCharacterError
            except anotherCharacterError:
                continue
            break

        playing = input("Do you want to play again? Type 'yes' or 'no': ")


