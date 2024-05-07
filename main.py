import tkinter as tk
from functools import partial

from GameLogic.board import Board as BoardEntity
from Controller.gameController import GameController
from View.board import Board as BoardView


def main():
    def open_board_view(level):
        board_window = tk.Toplevel()
        board = BoardView(board_window)
        board_entity = BoardEntity()
        game = GameController(board_entity, board, level)
        game.run()

    root = tk.Tk()
    root.title("Main View")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(pady=20)

    easy_button = tk.Button(frame, text="Easy", command=partial(open_board_view, 1))
    medium_button = tk.Button(frame, text="Medium", command=partial(open_board_view, 3))
    hard_button = tk.Button(frame, text="Hard", command=partial(open_board_view, 5))

    easy_button.grid(row=0, column=0, padx=10)
    medium_button.grid(row=0, column=1, padx=10)
    hard_button.grid(row=0, column=2, padx=10)

    root.mainloop()


if __name__ == "__main__":
    main()
