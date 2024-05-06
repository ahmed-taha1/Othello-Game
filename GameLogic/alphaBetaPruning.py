import copy
import math


def get_best_move(board, player_color, depth) -> (int, int):
    moves = get_possible_moves(board, player_color)
    max_score = -math.inf
    best_move = [-1,-1]

    alpha = - math.inf
    beta = math.inf
    for _, move in enumerate(moves):
        newBoard = update_board(board, move[0], move[1], player_color)
        move_score = alpha_beta_pruning(newBoard, player_color, alpha, beta, depth, False)
        if move_score > max_score:
            max_score = move_score
            best_move = move
    return best_move[0], best_move[1]


def alpha_beta_pruning(board, player_color, alpha, beta, depth, is_maximizing) -> int:
    moves = get_possible_moves(board, player_color)
    if depth == 0 or len(moves) == 0:
        return evaluate(board, player_color)

    if is_maximizing:
        max_score = -math.inf
        for _, move in enumerate(moves):
            newBoard = update_board(board, move[0], move[1], player_color)
            move_score = alpha_beta_pruning(newBoard, 1 - player_color, alpha, beta, depth - 1, False)
            max_score = max(max_score, move_score)
            alpha = max(alpha, move_score)
            if beta <= alpha:
                break
        return max_score

    else:
        min_score = math.inf
        for _, move in enumerate(moves):
            newBoard = update_board(board, move[0], move[1], player_color)
            move_score = alpha_beta_pruning(newBoard, 1 - player_color, alpha, beta, depth - 1, True)
            min_score = min(min_score, move_score)
            beta = min(beta, move_score)
            if beta <= alpha:
                break
        return min_score


def evaluate(board, player_color):
    rows = len(board)
    cols = len(board[0])
    cnt = 0
    for i in range(rows):
        for j in range(cols):
            cnt += (board[i][j] == player_color)
    return cnt


# tested
# encapsulate
def update_board(board, i, j, curr_player_color):
    newBoard = copy.deepcopy(board)
    flip_pieces(newBoard, i, j, curr_player_color, [0, 1])
    flip_pieces(newBoard, i, j, curr_player_color, [0, -1])
    flip_pieces(newBoard, i, j, curr_player_color, [-1, 0])
    flip_pieces(newBoard, i, j, curr_player_color, [1, 0])
    return newBoard


# tested
# encapsulate
def get_possible_moves(board, curr_player_color):
    valid_moves = []
    rows = len(board)
    cols = len(board[0])
    for i in range(rows):
        for j in range(cols):
            score = calc_move_score(board, i, j, curr_player_color)
            if score != 0:
                valid_moves.append([i, j])
    return valid_moves


# tested
def calc_move_score(board, i, j, curr_player_color):
    right = get_num_of_possible_flips(board, i, j, curr_player_color, [0, 1])
    left = get_num_of_possible_flips(board, i, j, curr_player_color, [0, -1])
    up = get_num_of_possible_flips(board, i, j, curr_player_color, [-1, 0])
    down = get_num_of_possible_flips(board, i, j, curr_player_color, [1, 0])
    return right + left + up + down


# tested
# encapsulate
def get_num_of_possible_flips(board, i, j, curr_player_color, change_of_coordinates):
    if curr_player_color == -1 or board[i][j] != -1:
        return 0
    rows = len(board)
    cols = len(board[0])
    another_color_cnt = 0
    another_player_color = 1 - curr_player_color
    i += change_of_coordinates[0]
    j += change_of_coordinates[1]
    while rows > i >= 0 and cols > j >= 0:
        if board[i][j] == -1:
            return 0
        if board[i][j] == curr_player_color:
            return another_color_cnt
        another_color_cnt += (board[i][j] == another_player_color)
        i += change_of_coordinates[0]
        j += change_of_coordinates[1]
    return 0


# tested
# encapsulate
def flip_pieces(board, i_play_position, j_play_position, curr_player_color, change_of_coordinates):
    rows = len(board)
    cols = len(board[0])
    another_player_color = 1 - curr_player_color
    count = get_num_of_possible_flips(board, i_play_position, j_play_position, curr_player_color, change_of_coordinates)
    if not count:
        return
    i = i_play_position
    j = j_play_position
    while rows > i >= 0 and cols > j >= 0:
        if board[i][j] == curr_player_color:
            break
        elif board[i][j] == another_player_color:
            board[i][j] = curr_player_color
        i += change_of_coordinates[0]
        j += change_of_coordinates[1]
    board[i_play_position][j_play_position] = curr_player_color

