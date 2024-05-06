class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.board = []
        for i in range(rows):
            self.board[i] = []
            for j in range(cols):
                self.board[i][j] = -1

    def add_piece(self, row, col, piece):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.board[row][col] = piece

    def get_piece_at(self, row, col):
        return self.board[row][col]

    def get_possible_moves(self, curr_player_color):
        valid_moves = []
        for i in range(self.rows):
            for j in range(self.cols):
                valid_right = self.is_valid_cell(i, j, curr_player_color, [0, 1])
                valid_left = self.is_valid_cell(i, j, curr_player_color, [0, -1])
                valid_up = self.is_valid_cell(i, j, curr_player_color, [-1, 0])
                valid_down = self.is_valid_cell(i, j, curr_player_color, [1, 0])
                if valid_right  or valid_left or valid_up or valid_down:
                    valid_moves.append([i, j])

    def get_num_of_flipped(self, row, col, curr_player_color, change_of_coordinates):
        another_color_cnt = 0
        another_player_color = 1 - curr_player_color
        i = row
        j = col
        while self.rows > i >= 0 and self.cols > j >= 0:
            if self.board[i][j] == curr_player_color:
                break
            i += change_of_coordinates[0]
            j += change_of_coordinates[1]
            another_color_cnt += (self.board[i][j] == another_player_color)

        return another_color_cnt
