import tkinter as tk
from View.piece import Piece


class Board:
    def __init__(self, master):
        self.rows = 8
        self.cols = 8
        self.master = master
        self.master.title("Board")
        self.board = []
        self.init_board()

    def cell_clicked(self, event):
        row = event.widget.grid_info()["row"]
        col = event.widget.grid_info()["column"]
        print(f"Cell clicked: Row {row}, Column {col}")
        self.add_piece(row, col)

    def add_piece(self, row, col):
        square = self.board[row][col]
        piece = Piece(square, "black")
        self.board[row][col].piece = piece

    def init_board(self):
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                square = tk.Canvas(self.master, width=50, height=50, bg="lightgreen")
                square.grid(row=i, column=j)
                square.bind("<Button-1>", self.cell_clicked)
                square.piece = None
                row.append(square)
            self.board.append(row)

