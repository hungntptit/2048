import pygame

pygame.font.init()
FONT_BIG = pygame.font.SysFont("consolas", 40, bold=True)
FONT = pygame.font.SysFont("consolas", 24, bold=True)
FONT_SMALL = pygame.font.SysFont("consolas", 14, bold=True)
FONT_TINY = pygame.font.SysFont("consolas", 16, bold=True)

# Colors
WHITE = (250, 250, 250)
BLACK = (21, 21, 21)
DARK = (75, 75, 75)
DARK_GRAY = (100, 100, 100)
GRAY = (150, 150, 150)
LIGHT_GRAY = (230, 230, 230)
RED = (244, 67, 54)
BLUE = (33, 150, 243)
YELLOW = (255, 241, 118)
LIGHT_YELLOW = (255, 249, 196)
PURPLE = (81, 45, 168)

color_dict = {
    0: (204, 192, 179),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46),
    "other": BLACK,
    "game_over": (238, 228, 218, 0.73),
}


FPS = 60
ROWS = 4
WIDTH = ROWS * 100
CELL_WIDTH = int(WIDTH / ROWS)

RESTART_BTN = pygame.Rect(WIDTH - 152, WIDTH + 110, 150, 36)

clock = pygame.time.Clock()


MOVES = ["up", "down", "left", "right"]
