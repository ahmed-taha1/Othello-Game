import copy


class Board:
    rows = 8
    cols = 8

    def __init__(self):
        self.grid = [[-1 for _ in range(self.cols)] for _ in range(self.rows)]
        self.grid[3][3] = 1
        self.grid[3][4] = 0
        self.grid[4][3] = 0
        self.grid[4][4] = 1

    def get_color_count(self, color):
        count = 0
        for i in range(self.rows):
            for j in range(self.cols):
                count += (color == self.grid[i][j])
        return count

    def add_piece(self, i, j, curr_player_color):
        def flip_pieces(i_play_position, j_play_position, color, change_of_coordinates):
            rows = len(self.grid)
            cols = len(self.grid[0])
            another_player_color = 1 - color
            count = self._count_possible_flips_in_direction(i_play_position, j_play_position, curr_player_color, change_of_coordinates)
            if not count:
                return
            temp_i = i_play_position
            temp_j = j_play_position
            while rows > temp_i >= 0 and cols > temp_j >= 0:
                if self.grid[temp_i][temp_j] == curr_player_color:
                    break
                elif self.grid[temp_i][temp_j] == another_player_color:
                    self.grid[temp_i][temp_j] = curr_player_color
                temp_i += change_of_coordinates[0]
                temp_j += change_of_coordinates[1]
            self.grid[i_play_position][j_play_position] = curr_player_color

        flip_pieces(i, j, curr_player_color, [0, 1])
        flip_pieces(i, j, curr_player_color, [0, -1])
        flip_pieces(i, j, curr_player_color, [-1, 0])
        flip_pieces(i, j, curr_player_color, [1, 0])

    def count_num_of_possible_flips(self, i_start, j_start, curr_player_color):
        right = self._count_possible_flips_in_direction(i_start, j_start, curr_player_color, [0, 1])
        left = self._count_possible_flips_in_direction(i_start, j_start, curr_player_color, [0, -1])
        up = self._count_possible_flips_in_direction(i_start, j_start, curr_player_color, [-1, 0])
        down = self._count_possible_flips_in_direction(i_start, j_start, curr_player_color, [1, 0])
        return right + left + up + down

    def _count_possible_flips_in_direction(self, i, j, curr_player_color, change_of_coordinates):
        if curr_player_color == -1 or self.grid[i][j] != -1:
            return 0
        another_color_cnt = 0
        another_player_color = 1 - curr_player_color
        i += change_of_coordinates[0]
        j += change_of_coordinates[1]
        while self.rows > i >= 0 and self.cols > j >= 0:
            if self.grid[i][j] == -1:
                return 0
            if self.grid[i][j] == curr_player_color:
                return another_color_cnt
            another_color_cnt += (self.grid[i][j] == another_player_color)
            i += change_of_coordinates[0]
            j += change_of_coordinates[1]
        return 0

    def get_possible_cell_moves(self, curr_player_color):
        valid_moves = []
        for i in range(self.rows):
            for j in range(self.cols):
                score = self.count_num_of_possible_flips(i, j, curr_player_color)
                if score != 0:
                    valid_moves.append([i, j])
        return valid_moves

    def clone(self):
        return copy.deepcopy(self)
