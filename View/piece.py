class Piece:
    piece_id = 0

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.render_piece()

    def render_piece(self):
        x, y = 50, 50
        radius = 30
        self.piece_id = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=self.color)
