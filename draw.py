from config import *


def draw_cell(SCREEN, cell_center, value):
    color = color_dict[value]
    cell_rect = pygame.Rect(0, 0, CELL_WIDTH - 8, CELL_WIDTH - 8)
    cell_rect.center = cell_center
    pygame.draw.rect(SCREEN, color, cell_rect, 0, 5)


def draw_board(SCREEN, board):
    for i in range(4):
        for j in range(4):
            cell_center = (
                int(CELL_WIDTH * (j + 0.5)) + 4,
                int(CELL_WIDTH * (i + 0.5)) + 80,
            )
            value = board[i][j]
            draw_cell(SCREEN, cell_center, value)
            color = DARK if value <= 4 else WHITE
            if value > 0:
                txt = FONT_BIG.render(f"{value}", True, color)
                txt_rect = txt.get_rect()
                txt_rect.center = cell_center
                SCREEN.blit(txt, txt_rect.topleft)


def draw_guide(SCREEN):
    guide_txt = FONT_SMALL.render("r: restart", True, BLACK)
    SCREEN.blit(guide_txt, (8, WIDTH + 90))
    guide_txt = FONT_SMALL.render("a: toggle auto", True, BLACK)
    SCREEN.blit(guide_txt, (8, WIDTH + 110))
    guide_txt = FONT_SMALL.render("space: auto 1 step", True, BLACK)
    SCREEN.blit(guide_txt, (8, WIDTH + 130))


def draw_input(SCREEN, keys):
    key_txt = FONT.render("", True, BLACK)
    if keys[pygame.K_UP]:
        key_txt = FONT_SMALL.render("up", True, BLACK)
    elif keys[pygame.K_DOWN]:
        key_txt = FONT_SMALL.render("down", True, BLACK)
    elif keys[pygame.K_LEFT]:
        key_txt = FONT_SMALL.render("left", True, BLACK)
    elif keys[pygame.K_RIGHT]:
        key_txt = FONT_SMALL.render("right", True, BLACK)
    elif keys[pygame.K_r]:
        key_txt = FONT_SMALL.render("restart", True, BLACK)
    elif keys[pygame.K_a]:
        key_txt = FONT_SMALL.render("toggle auto", True, BLACK)
    elif keys[pygame.K_SPACE]:
        key_txt = FONT_SMALL.render("auto 1 step", True, BLACK)
    key_txt_rect = key_txt.get_rect()
    key_txt_rect.topleft = (WIDTH - 100, WIDTH + 115)
    SCREEN.blit(key_txt, key_txt_rect.topleft)


even = True


def draw_move(SCREEN, move=None):
    global even
    if move:
        key_txt = FONT.render(f"{move}", True, BLACK if even else BLUE)
        key_txt_rect = key_txt.get_rect()
        key_txt_rect.topleft = (WIDTH - 80, 40)
        SCREEN.blit(key_txt, key_txt_rect.topleft)
        even = not even


def draw_points(SCREEN, points):
    points_txt = FONT.render(f"SCORES: {points}", True, BLACK)
    points_txt_rect = points_txt.get_rect()
    points_txt_rect.topleft = (10, 10)
    SCREEN.blit(points_txt, points_txt_rect.topleft)


def draw_end(SCREEN, end_game):
    if end_game == 2:
        win_txt = FONT.render(f"YOU WIN!", True, BLUE)
        win_txt_rect = win_txt.get_rect()
        win_txt_rect.topleft = (10, 45)
        SCREEN.blit(win_txt, win_txt_rect.topleft)
    elif end_game == 1:
        lose_txt = FONT.render(f"YOU LOSE!", True, RED)
        lose_txt_rect = lose_txt.get_rect()
        lose_txt_rect.topleft = (10, 45)
        SCREEN.blit(lose_txt, lose_txt_rect.topleft)


def draw_result(SCREEN, result):
    y = 10
    for i in result:
        score_txt = FONT.render(f"{i[0]}: {i[1]}", True, BLACK)
        score_txt_rect = score_txt.get_rect()
        score_txt_rect.topleft = (10, y)
        y += 10
        SCREEN.blit(score_txt, score_txt_rect.topleft)


def draw_all(SCREEN, board, keys):
    draw_board(SCREEN, board)
    draw_input(SCREEN, keys)
    draw_guide(SCREEN)
