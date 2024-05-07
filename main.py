import tkinter as tk
from functools import partial
from GameLogic.board import Board as BoardEntity
from Controller.boardController import BoardController
from View.board import Board as BoardView
from tkinter import font


def main():
    def open_board_view(level):
        board_frame.tkraise()
        board = BoardView(board_frame)
        board_entity = BoardEntity()
        board_controller = BoardController(board_entity, board, level)
        board_controller.run()

    root = tk.Tk()
    root.geometry("830x830")
    root.title("Othello Game")
    root.resizable(False, False)

    levels_page = tk.Frame(root)  # Frame for difficulty selection
    board_frame = tk.Frame(root)  # Frame for the board

    levels_page.grid(row=0, column=0, sticky=tk.NSEW)
    board_frame.grid(row=0, column=0, sticky=tk.NSEW)

    # Elements for the levels page (difficulty selection)
    tk.Label(levels_page, text="Select Difficulty", font=("Arial", 24)).pack(pady=20)

    # Buttons to select difficulty and open the board view
    easy_button = tk.Button(levels_page, text="Easy", font=font.Font(size=25), command=lambda: open_board_view(1))
    medium_button = tk.Button(levels_page, text="Medium", font=font.Font(size=25), command=lambda: open_board_view(3))
    hard_button = tk.Button(levels_page, text="Hard", font=font.Font(size=25), command=lambda: open_board_view(5))

    # Arrange buttons on the levels page
    easy_button.pack(pady=50, padx=350)
    medium_button.pack(pady=50, padx=350)
    hard_button.pack(pady=50, padx=350)

    # Start by showing the levels page
    levels_page.tkraise()

    # Start the Tkinter event loop
    root.mainloop()


if __name__ == "__main__":
    main()
