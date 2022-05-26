from config import *
from calculate import *
import random
from math import inf
from move import *


def add_random_tile(board):
    global end_game
    empty_positions = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                empty_positions.append([i, j])
    if not empty_positions:
        end_game = 1
        return
    i = random.choice(range(len(empty_positions)))
    pos = empty_positions[i]
    ran = random.random()
    if ran < 0.9:
        board[pos[0]][pos[1]] = 2
    else:
        board[pos[0]][pos[1]] = 4


def simulate_move(board, move):
    if move == "up":
        return move_up(board)
    elif move == "down":
        return move_down(board)
    elif move == "left":
        return move_left(board)
    elif move == "right":
        return move_right(board)


def is_end(board):
    for move in MOVES:
        if simulate_move(board, move) != board:
            return False
    return True


def get_empty_cells(board):
    empty_cells = []
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                empty_cells.append([i, j])
    # random.shuffle(empty_cells)
    return empty_cells


def board_score(board, depth, limit):
    if depth >= limit:
        return heuristic(board)
    total_score = 0
    empty_cells = get_empty_cells(board)
    for cell in empty_cells:
        i, j = cell[0], cell[1]
        new_board_2 = [x[:] for x in board]
        new_board_2[i][j] = 2
        move_score_2 = move_score(new_board_2, depth, limit)
        total_score += 0.9 * move_score_2

        new_board_4 = [x[:] for x in board]
        new_board_4[i][j] = 4
        move_score_4 = move_score(new_board_4, depth, limit)
        total_score += 0.1 * move_score_4
    return total_score


def heuristic(board):
    score = weight_sum(board)
    score -= 10**8 * different(board)
    score += 10**6 * count_empty_cells(board)
    if any(2048 in row for row in board):
        score = inf
    return score


def move_score(board, depth, limit):
    best_score = 0
    for move in MOVES:
        new_board = simulate_move(board, move)
        if new_board != board:
            score = board_score(new_board, depth + 1, limit)
            best_score = max(best_score, score)
    return best_score


def choose_next_move(board):
    best_move = None
    best_score = -inf
    for move in MOVES:
        new_board = simulate_move(board, move)
        if new_board == board:
            continue
        # limit is even
        score = board_score(new_board, 0, 1)
        if score > best_score:
            best_score = score
            best_move = move
    # print(best_score, best_move)
    return best_move
