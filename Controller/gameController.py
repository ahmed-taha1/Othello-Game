import time

from GameLogic.board import Board as BoardEntity
from View.board import Board as BoardView
from GameLogic.alphaBetaPruning import get_best_move


class GameController:
    player_id = 0
    robot_id = 1
    depth = 1

    def __init__(self, board_entity: BoardEntity, board_view: BoardView):
        self.board_entity: BoardEntity = board_entity
        self.board_view: BoardView = board_view
        self.init_view_callbacks()
    
    def init_view_callbacks(self):
        self.board_view.set_cell_click_callback(self.play)

    def run(self):
        self.update_ui_grid()
        self.display_plays()
        self.board_view.render()

    def play(self, row, col):
        self.clear_cells()
        if not self.board_entity.is_move_valid(row, col, self.player_id):
            return

        # add current play to the board
        self.board_entity.add_piece(row, col, self.player_id)
        self.update_ui_grid()

        # make the computer plays
        robot_move = get_best_move(self.board_entity, self.robot_id, self.depth)
        if robot_move != [-1, -1]:
            self.board_entity.add_piece(robot_move[0], robot_move[1], self.robot_id)
        self.update_ui_grid()
        # display next possible plays
        self.display_plays()
        return 0

    def update_ui_grid(self):
        grid = self.board_entity.get_grid()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == self.player_id:
                    self.board_view.set_human_piece(i, j)
                elif grid[i][j] == self.robot_id:
                    self.board_view.set_ai_piece(i, j)

    def display_plays(self):
        moves = self.board_entity.get_possible_cell_moves(self.player_id)
        print(moves)
        for move in moves:
            self.board_view.highlight_cell(move[0], move[1])

    def clear_cells(self):
        grid = self.board_entity.get_grid()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.board_view.clear_cell_highlight(i, j)