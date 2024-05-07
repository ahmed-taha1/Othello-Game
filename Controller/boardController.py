from GameLogic.board import Board as BoardEntity
from View.board import Board as BoardView
from GameLogic.alphaBetaPruning import get_best_move


class BoardController:
    player_id = 0
    robot_id = 1

    def __init__(self, board_entity: BoardEntity, board_view: BoardView, level: int):
        self.depth = level
        self.board_entity: BoardEntity = board_entity
        self.board_view: BoardView = board_view
        self.init_view_callbacks()
    
    def init_view_callbacks(self):
        self.board_view.set_cell_click_callback(self.human_play)

    def run(self):
        self.update_ui_grid()
        self.display_plays()
        self.board_view.render()

    def human_play(self, row, col):
        if not self.board_entity.is_move_valid(row, col, self.player_id):
            return
        # remove highlighted cells
        self.clear_cells()

        # add current play to the board
        self.board_entity.add_piece(row, col, self.player_id)
        self.update_ui_grid()

        self.board_view.master.after(500, self.ai_play)

    def ai_play(self):
        # make the computer plays till the human have moves to do or till the robot have no moves to do
        while True:
            robot_move = get_best_move(self.board_entity, self.robot_id, self.depth)
            if robot_move != [-1, -1]:
                self.board_entity.add_piece(robot_move[0], robot_move[1], self.robot_id)
            self.update_ui_grid()
            if (len(self.board_entity.get_possible_cell_moves(self.player_id)) > 0 or
                    len(self.board_entity.get_possible_cell_moves(self.robot_id)) == 0):
                break
        # display next possible plays for the human
        self.display_plays()

        # if they have no moves terminate the game
        if (len(self.board_entity.get_possible_cell_moves(self.player_id)) == 0 and
                len(self.board_entity.get_possible_cell_moves(self.robot_id)) == 0):
            self.end_game()
            return

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
        for move in moves:
            self.board_view.highlight_cell(move[0], move[1])

    def clear_cells(self):
        grid = self.board_entity.get_grid()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.board_view.clear_cell_highlight(i, j)

    def end_game(self):
        human_score = self.board_entity.get_color_count(self.player_id)
        robot_score = self.board_entity.get_color_count(self.robot_id)
        message = ""
        if human_score > robot_score:
            message = "you wins"
        elif human_score == robot_score:
            message = "draw"
        elif human_score < robot_score:
            message = "you lose"

        self.board_view.end_game(message)
