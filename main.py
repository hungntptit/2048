import pygame
import sys
from game_funtion import *
from draw import *
from config import *

auto = -1


def check_events():
    global board, end_game, auto, points
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYUP:
            if auto == -1:
                new_board = [x[:] for x in board]
                if event.key == pygame.K_UP:
                    new_board = simulate_move(new_board, "up")
                elif event.key == pygame.K_DOWN:
                    new_board = simulate_move(new_board, "down")
                elif event.key == pygame.K_LEFT:
                    new_board = simulate_move(new_board, "left")
                elif event.key == pygame.K_RIGHT:
                    new_board = simulate_move(new_board, "right")
                if new_board != board:
                    points += new_score(board, new_board)
                    add_random_tile(new_board)
                board = new_board
            if event.key == pygame.K_r:
                auto = -1
                reset()
            elif event.key == pygame.K_a:
                auto = -auto
            elif event.key == pygame.K_SPACE:
                auto = 0


def reset():
    global board, end_game, points
    board = [[0 for i in range(4)] for j in range(4)]
    add_random_tile(board)
    add_random_tile(board)
    end_game = 0
    points = 0


def auto_play(board):
    global points
    next_move = None
    if end_game == 0:
        next_move = choose_next_move(board)
        new_board = simulate_move(board, next_move)
        if new_board != board and new_board != None:
            points += new_score(board, new_board)
            add_random_tile(new_board)
            board = new_board
    return board, next_move


board = [[0 for i in range(4)] for j in range(4)]
points = 0
end_game = 0

if __name__ == "__main__":

    pygame.init()
    SCREEN = pygame.display.set_mode((WIDTH + 8, WIDTH + 160))
    pygame.display.set_caption("2048")

    reset()
    times = 0
    result = []
    while True:
        SCREEN.fill(WHITE)
        check_events()
        if times > 100:
            draw_result(SCREEN, result)
            continue
        next_move = None
        if auto == 1:
            board, next_move = auto_play(board)
        elif auto == 0:
            board, next_move = auto_play(board)
            auto = -1
        keys = pygame.key.get_pressed()
        draw_all(SCREEN, board, keys)
        draw_points(SCREEN, points)
        draw_move(SCREEN, next_move)
        if is_end(board):
            end_game = 1
        if any(2048 in x for x in board):
            end_game = 2
        if end_game > 0:
            draw_end(SCREEN, end_game)
            # if auto == 1:
            #     times += 1
            #     max_score = max(max(i) for i in board)
            #     print(max_score)
            #     reset()
        pygame.display.update()
        clock.tick(FPS)
