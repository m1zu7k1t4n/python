# coding : utf-8
import numpy as np


class Puzzle_No2(object):
    shape_1 = "12:4 39 12 13 12 0 3 39 3:5 3 25 6 20 1 3 12 3 8 25:4 13 31 7 31 1 3 13 1:5 9 14 4 14 4 10 0 10 9 2:6 4 2 28 2 25 7 25 14 7 14 7 7:4 52 1 52 6 2 6 6 1:4 1 10 1 3 23 3 23 10:4 4 6 4 0 10 0 10 6:6 1 8 5 7 5 3 9 3 10 18 2 18:5 1 50 1 2 14 23 13 28 6 39:4 13 5 3 6 3 1 13 1:4 2 8 4 2 13 2 11 8"
    shape_2 = "12:5 11 15 2 30 6 6 9 1 14 12:5 5 24 9 0 13 6 9 28 2 29:4 9 10 7 16 3 6 12 0:4 2 3 33 3 33 10 2 10:5 4 8 8 2 13 2 17 8 3 23:4 10 1 10 12 2 12 1 1:4 23 3 23 8 6 8 3 3:5 15 12 2 3 40 3 40 7 28 12:4 12 11 3 11 6 1 14 1:4 9 26 2 26 2 2 11 2:4 3 15 5 3 21 3 18 6:4 2 0 7 3 7 22 2 19"
    shape_3 = "12:5 3 21 2 4 6 10 9 15 4 32:5 16 2 17 9 0 15 0 10 5 9:4 13 1 7 18 6 11 2 1:6 18 24 13 24 12 31 3 25 0 12 18 3:4 6 28 1 28 1 4 6 1:6 11 17 3 17 6 4 10 4 9 8 13 8:5 31 23 3 17 18 3 37 3 37 23:4 3 2 16 2 16 8 5 8:4 18 1 18 9 1 8 1 0:5 1 1 21 4 30 5 25 8 1 6:4 6 21 0 21 0 4 5 4:3 4 13 4 0 25 0"
    shape_4 = "9:4 2 3 6 3 10 4 2 13:4 4 1 21 1 21 8 1 8:6 4 0 16 0 16 5 9 5 9 16 4 16:8 9 4 18 4 18 15 11 15 2 14 5 11 5 7 9 8:5 13 12 3 12 3 5 6 0 13 0:6 9 27 7 18 5 8 3 2 9 4 12 24:3 11 3 11 21 2 21:4 14 13 0 13 0 1 14 1:5 1 1 11 1 11 15 6 19 6 13:8 0 0 100 0 100 64 0 64 0 59 4 59 7 52 0 52"

    level_1 = "9:4 0 59 27 59 24 64 0 64:4 7 52 24 52 24 59 4 59:5 34 12 40 16 40 21 34 25 19 26:4 24 52 46 52 46 59 24 59:4 27 59 46 59 43 64 24 64:6 46 59 46 52 64 52 64 59 67 64 43 64:4 64 52 95 52 95 59 64 59:4 64 59 84 59 84 64 67 64:6 84 59 95 59 95 52 100 52 100 64 84 64"
    level_2 = "10:4 0 0 6 0 6 6 0 6:5 0 6 6 6 34 12 19 26 0 26:4 0 26 14 26 14 38 0 38:5 0 38 14 38 18 43 12 43 0 48:4 36 0 34 12 6 6 6 0:4 36 0 52 0 49 3 34 12:5 52 0 100 0 79 13 74 12 63 5:6 72 19 79 18 79 13 100 13 91 31 78 28:3 100 0 100 13 79 13:3 100 13 100 31 91 31"
    level_3 = "9:5 0 48 12 43 25 43 38 52 0 52:4 14 38 64 38 64 43 18 43:4 25 43 64 43 64 52 38 52:6 62 32 68 34 78 36 87 38 84 41 64 38:5 64 38 84 41 93 42 88 45 64 43:4 64 43 88 45 88 52 64 52:6 78 28 91 31 91 35 87 34 87 38 78 36:8 87 38 87 34 91 35 91 31 100 31 100 42 93 42 84 41:5 88 45 93 42 100 42 100 52 88 52"
    level_4 = "9:5 14 26 19 26 19 30 23 30 14 38:4 14 38 23 30 24 34 24 38:6 19 26 34 25 34 33 24 34 23 30 19 30:4 24 34 34 33 34 38 24 38:4 34 33 51 32 51 38 34 38:5 34 12 58 8 63 5 62 12 40 16:5 49 3 52 0 63 5 58 8 34 12:4 51 32 62 32 64 38 51 38:5 63 5 74 12 79 13 79 18 62 12"

    def __init__(self):
        self.piece = list()
        self.frame = tuple()

        for variable in [self.shape_1, self.shape_2, self.shape_3, self.shape_4]:
            shape_tuple = variable.split(":")[1:]
            for piece_tuple in shape_tuple:
                piece_tuple = piece_tuple.split(" ")
                grid_num = piece_tuple[0]
                piece_data = tuple(
                    [int(grid_num),
                     tuple([(int(piece_tuple[x]), int(piece_tuple[x + 1])) for x in range(1, len(piece_tuple), 2)])])
                self.piece.append(piece_data)
        self.frame = self.piece[-1]
        self.piece = self.piece[:-1]

    def getFrame(self) -> np.ndarray:
        self.board = np.zeros((65, 101), dtype='int8')
        for num in range(-1, self.frame[0] - 1):
            x1 = self.frame[1][num][0]
            y1 = self.frame[1][num][1]
            x2 = self.frame[1][num + 1][0]
            y2 = self.frame[1][num + 1][1]
            x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

            if x1 == x2:
                left = min(y1, y2)
                right = max(y1, y2)
                for v in range(left, right + 1):
                    self.board[v][x1] = 1
            elif y1 == y2:
                left = min(x1, x2)
                right = max(x1, x2)
                for v in range(left, right + 1):
                    self.board[y1][v] = 1
            else:
                y = y1
                yp = int((y2 - y1) / (x2 - x1))
                for x in range(x1 + 1, x2 + 1):
                    if yp >= 0:
                        for m in range(1, yp + 1):
                            y += 1
                            self.board[y][x] = 1
                    else:
                        for m in range(1, -yp + 1):
                            y -= 1
                            self.board[y][x] = 1

        self.board_fill(50, 30, 101, 65, self.board)

        return self.board * -1

    def getPiece(self) -> tuple:
        return self.piece

    def getPieceMatrix(self) -> np.ndarray:
        PieceMat = list()
        for piece_one in self.piece:
            self.getPieceMatrix(piece_one)

    def getLevel(self, lv):
        if lv == 1:
            pass
        elif lv == 2:
            pass
        elif lv == 3:
            pass
        elif lv == 4:
            pass

    def board_fill(self, s_x, s_y, Width, Height, board):

        INF = 100000000

        distance = [[INF for i in range(Width)] for j in range(Height)]

        def bfs():
            queue = []

            queue.insert(0, (s_x, s_y))

            distance[s_y][s_x] = 0
            board[s_y][s_x] = 1

            while len(queue):
                x, y = queue.pop()

                for i in range(0, 4):
                    nx, ny = x + [1, 0, -1, 0][i], y + [0, 1, 0, -1][i]

                    if (0 <= nx and nx < Width and 0 <= ny and ny < Height and
                                board[ny][nx] == 0 and distance[ny][nx] == INF):
                        queue.insert(0, (nx, ny))
                        distance[ny][nx] = distance[y][x] + 1
                        board[ny][nx] = 1

        return bfs()

    def pieceWrite(self, piece_one) -> np.ndarray:
        xs, xm, ys, ym = 101, 0, 65, 0
        for x, y in piece_one[1]:
            xs = x if xs > x else xs
            xm = x if xm < x else xm
            ys = y if ys > y else ys
            ym = y if ym < y else ym
        piece_mat = np.zeros((ym - ys, xm - xs), dtype='int8')
        for i in range(piece_one[0]):
            piece_one[1][i][0] -= xs
            piece_one[1][i][1] -= ys
        for num in range(-1, self.piece_one[0] - 1):
            x1 = self.piece_one[1][num][0]
            y1 = self.piece_one[1][num][1]
            x2 = self.piece_one[1][num + 1][0]
            y2 = self.piece_one[1][num + 1][1]
            x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

            if x1 == x2:
                left = min(y1, y2)
                right = max(y1, y2)
                for v in range(left, right + 1):
                    piece_mat[v][x1] = 1
            elif y1 == y2:
                left = min(x1, x2)
                right = max(x1, x2)
                for v in range(left, right + 1):
                    piece_mat[y1][v] = 1
            else:
                y = y1
                yp = int((y2 - y1) / (x2 - x1))
                for x in range(x1 + 1, x2 + 1):
                    if yp >= 0:
                        for m in range(1, yp + 1):
                            y += 1
                            piece_mat[y][x] = 1
                    else:
                        for m in range(1, -yp + 1):
                            y -= 1
                            piece_mat[y][x] = 1
        x1, y1 = piece_one[1][0]
        for pair in piece_one[1][1:]:
            if (not x1 == pair[0]) and (not y1 == pair[1]):
                x2, y2 = pair
        cx, cy = x2 - x1, y2 - y1
        bias = np.array(cx,cy).astype(bool)

        self.board_fill(50, 30, 101, 65, piece_mat)
        return piece_mat
