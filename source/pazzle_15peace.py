# coding=utf-8
import random
import time
import copy


def check(board):
    for i, v in enumerate(reduce(lambda a, b: a + b, board)):
        if (i + 1) != v:
            return False
    return True


def check_line(board):
    correct = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    lines = []
    for i, v in enumerate(correct):
        if v == board[i]:
            lines.append(i)
    return lines


def find_mover(board, n):
    for i in xrange(len(board)):
        if n in board[i]:
            return i, board[i].index(n)


def random_walk(board, from_p, to_p, fixed=[]):
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    res = []
    mover = find_mover(board, 16)
    while len([v for i, v in enumerate(to_p) if board[v[0]][v[1]] == from_p[i]]) != len(to_p):
        move = moves[random.randint(0, 3)]
        moved = mover[0] + move[0], mover[1] + move[1]
        if moved in fixed:
            continue
        if 0 <= moved[0] < 4 and 0 <= moved[1] < 4:
            board[moved[0]][moved[1]], board[mover[0]][mover[1]]\
                = board[mover[0]][mover[1]], board[moved[0]][moved[1]]

            res.append(board[mover[0]][mover[1]])
            mover = mover[0] + move[0], mover[1] + move[1]
    return res, board


def solver(board):
    fixed = []
    to_list = [[(0, 0, 1)], [(0, 1, 2)], [(0, 2, 3), (0, 3, 4)],
               [(1, 0, 5)], [(1, 1, 6)], [(1, 2, 7), (1, 3, 8)],
               [(2, 0, 9), (3, 0, 13)], [(2, 1, 10), (3, 1, 14)],
               [(2, 2, 11), (2, 3, 12), (3, 2, 15)]]
    ans = []
    for i in to_list:
        froms = [j[2] for j in i]
        tos = [(j[0], j[1]) for j in i]
        res, board = random_walk(board, froms, tos, fixed)
        ans += res
        fixed += tos
    return ans


def board_input():
    board = []
    for i in xrange(4):
        board.append(map(int, raw_input().replace('*', '16').split()))
    return board


def board_output(board):
    for i in board:
        print i
    print "-----------"


if __name__ == "__main__":
    start = time.time()
    ans_len = 10000000
    res = []
    board = board_input()
    board_tmp = copy.deepcopy(board)
    while True:
        board = copy.deepcopy(board_tmp)
        ans = solver(board)
        if len(ans) < ans_len:
            res = ans
            ans_len = len(res)
        if time.time() - start > 7:
            break
    print '\n'.join([str(i) for i in res])
