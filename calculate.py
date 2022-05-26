W = [
    [4**16, 4**15, 4**14, 4**13],
    [4**12, 4**11, 4**10, 4**9][::-1],
    [4**8, 4**7, 4**6, 4**5],
    [4**4, 4**3, 4**2, 4**1][::-1],
]


def weight_sum(board):
    sum = 0
    for i in range(4):
        for j in range(4):
            sum += W[i][j] * board[i][j]
    return sum


def diff_in_row(board, row):
    d = 0
    for i in range(3):
        d += abs(board[row][i] - board[row][i + 1])
    return d


def transpose(board):
    t_board = [x[:] for x in board]
    t_board = [*zip(*t_board)]
    return t_board


def different(board):
    d = 0
    for row in range(4):
        d += diff_in_row(board, row)
    t_board = transpose(board)
    for col in range(4):
        d += diff_in_row(t_board, col)
    return d


def count_empty_cells(board):
    return sum(x.count(0) for x in board)


def new_score(old, new):
    list_old = []
    for row in old:
        list_old.extend(row)
    list_old.sort()
    list_new = []
    for row in new:
        list_new.extend(row)
    list_new.sort()
    i = 0
    while i < len(list_old):
        if list_old[i] in list_new:
            list_new[list_new.index(list_old[i])] = -1
            list_old[i] = -2
        else:
            i += 1
    # print(list_old, list_new)
    tmp = list(filter(lambda x: x > 0, list_new))
    # print(sum(tmp))
    return sum(tmp)
