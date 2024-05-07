import math
from GameLogic.board import Board


def get_best_move(board: Board, player_color, depth) -> (int, int):
    moves = board.get_possible_cell_moves(player_color)
    max_score = -math.inf
    best_move = [-1, -1]

    alpha = - math.inf
    beta = math.inf
    for move in moves:
        clonedBoard = board.clone()
        clonedBoard.add_piece(move[0], move[1], player_color)
        move_score = alpha_beta_pruning(clonedBoard, player_color, alpha, beta, depth, False)
        if move_score > max_score:
            max_score = move_score
            best_move = move
    return best_move[0], best_move[1]


def alpha_beta_pruning(board: Board, player_color, alpha, beta, depth, is_maximizing) -> int:
    moves = board.get_possible_cell_moves(player_color)
    if depth == 0 or len(moves) == 0:
        return evaluate(board, player_color)

    if is_maximizing:
        max_score = -math.inf
        for move in moves:
            clonedBoard = board.clone()
            clonedBoard.set_human_piece(move[0], move[1], player_color)
            move_score = alpha_beta_pruning(clonedBoard, 1 - player_color, alpha, beta, depth - 1, False)
            max_score = max(max_score, move_score)
            alpha = max(alpha, move_score)
            if beta <= alpha:
                break
        return max_score

    else:
        min_score = math.inf
        for _, move in enumerate(moves):
            clonedBoard = board.clone()
            clonedBoard.add_piece(move[0], move[1], player_color)
            move_score = alpha_beta_pruning(clonedBoard, 1 - player_color, alpha, beta, depth - 1, True)
            min_score = min(min_score, move_score)
            beta = min(beta, move_score)
            if beta <= alpha:
                break
        return min_score


def evaluate(board: Board, player_color):
    return board.get_color_count(player_color)
