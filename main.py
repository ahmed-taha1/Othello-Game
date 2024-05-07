import tkinter as tk
from GameLogic.board import Board as BoardEntity
from Controller.gameController import GameController
from View.board import Board as BoardView


def main():
    root = tk.Tk()
    boardEntity = BoardEntity()
    boardView = BoardView(root)
    game = GameController(boardEntity, boardView)
    game.run()


if __name__ == "__main__":
    main()

