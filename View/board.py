import tkinter as tk
from View.piece import Piece
import time

class Board:
    rows = 8
    cols = 8
    click_callback = None
    cell_color = "lightgreen"
    highlight_color = "grey"
    human_color = "black"
    ai_color = "white"

    def __init__(self, master):
        self.master = master
        self.board = []
        self.init_board()
        self.result_label = tk.Label(self.master, text="", font=("Arial", 45),bg="lightgreen",fg="black" ,width=5,height=3, borderwidth=2, relief="solid")

    def init_board(self):
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                square = tk.Canvas(self.master, width=100, height=100, bg=self.cell_color)
                square.grid(row=i, column=j)
                square.bind("<Button-1>", self.cell_clicked)
                square.piece = None
                row.append(square)
            self.board.append(row)

    def render(self):
        self.master.mainloop()

    def highlight_cell(self, row, col):
        canvas_widget = self.board[row][col]
        canvas_widget.config(bg=self.highlight_color)

    def clear_cell_highlight(self, row, col):
        canvas_widget = self.board[row][col]
        canvas_widget.config(bg=self.cell_color)

    def set_human_piece(self, row, col):
        square = self.board[row][col]
        piece = Piece(square, self.human_color)
        self.board[row][col].piece = piece
        time.sleep(0.05)
        square.update()

    def set_ai_piece(self, row, col):
        square = self.board[row][col]
        piece = Piece(square, self.ai_color)
        self.board[row][col].piece = piece
        time.sleep(0.05)
        square.update()

    def cell_clicked(self, event):
        row = event.widget.grid_info()["row"]
        col = event.widget.grid_info()["column"]
        print(f"Cell clicked: Row {row}, Column {col}")
        self.click_callback(row, col)

    def set_cell_click_callback(self, callback):
        self.click_callback = callback

    def end_game(self, message):
        self.result_label.config(text=message)
        self.result_label.grid(row=2, column=2, columnspan=self.rows // 2,rowspan=self.cols // 2,sticky="EW")
