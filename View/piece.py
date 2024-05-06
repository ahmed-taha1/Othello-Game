import tkinter as tk


class Piece:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.render_piece()
        self.piece_id

    def render_piece(self):
        self.piece_id = self.canvas.create_text(30, 30, text="♟", font=("Arial", 20), fill=self.color)