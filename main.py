from game import Game
from menu import Menu
import sys

if __name__ == "__main__":
    menu = Menu()

    param = menu.run()

    if param[0] == "quit":
        sys.exit()

    print(param)

    game = Game(param[1], param[0])
    game.mainLoop()