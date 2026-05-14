import tkinter as tkint
from views.tkinter_view import TkinterView
from config import BOARD_SIZE, WIN_LENGTH, validate_config
from controllers.game_controller import GameController

def main():
    validate_config()
    root = tkint.Tk()
    controller = GameController(BOARD_SIZE, WIN_LENGTH)
    TkinterView(root, controller)
    root.mainloop()
if __name__ == "__main__":
    main()