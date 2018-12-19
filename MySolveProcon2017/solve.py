import numpy as np
import matplotlib.pyplot as plt
from qr_info import Puzzle_No2
import matplotlib.pyplot as plt

"""
-1 空白　てか入ってない
0  壁　　枠
1~ ピースの識別番号
"""


def solve():
    pn2 = Puzzle_No2()
    board = pn2.getFrame()
    x = np.arange(101)
    y = np.arange(65)
    X, Y = np.meshgrid(x, y)
    plt.pcolor(X, Y, board)
    plt.colorbar()
    plt.show()


def printf(board):
    with open("test.txt", "w") as f:
        for col in board:
            for one in col:
                if one == -1:
                    f.write("#" + ".")
                else:
                    f.write(str(one) + ".")
            f.write("\n")


def main():
    solve()


if __name__ == '__main__':
    main()
