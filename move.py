def move_up(board):
    b = [x[:] for x in board]
    b = rotate_right(b)
    b = move_right(b)
    b = rotate_right(b)
    b = rotate_right(b)
    b = rotate_right(b)
    return b


def move_down(board):
    b = [x[:] for x in board]
    b = rotate_right(b)
    b = move_left(b)
    b = rotate_right(b)
    b = rotate_right(b)
    b = rotate_right(b)
    return b


def move_left(board):
    b = [x[:] for x in board]
    shift_left(b)
    for i in range(4):
        for j in range(3):
            if b[i][j] == b[i][j + 1] and b[i][j] != 0:
                b[i][j] *= 2
                b[i][j + 1] = 0
                j = 0
    shift_left(b)
    return b


def move_right(board):
    b = [x[:] for x in board]
    shift_right(b)
    for i in range(4):
        for j in range(3, 0, -1):
            if b[i][j] == b[i][j - 1] and b[i][j] != 0:
                b[i][j] *= 2
                b[i][j - 1] = 0
                j = 0
    shift_right(b)
    return b


def shift_right(board):
    for row in range(4):
        tmp = list(filter(lambda x: x != 0, board[row]))
        tmp[0:0] = [0 for x in range(4 - len(tmp))]
        board[row] = tmp
    return board


def shift_left(board):
    for row in range(4):
        tmp = list(filter(lambda x: x != 0, board[row]))
        tmp.extend([0 for x in range(4 - len(tmp))])
        board[row] = tmp
    return board


def rotate_right(board):
    b = list(zip(*board[::-1]))
    b = [list(i) for i in b]
    return b
