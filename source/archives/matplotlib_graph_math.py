import matplotlib.pyplot as plt
import numpy as np
from ipywidgets import interact


def mathplot(time):
    # 媒介変数の範囲設定
    r = 1
    t = np.arange(time, time + 0.05, 0.01)
    # x,yの定式化
    x = r * (1 + np.cos(t)) * np.cos(t)
    y = r * (1 + np.cos(t)) * np.sin(t)
    print(x[0], y[0])
    # 軸の縦横比の調整
    plt.gca().set_aspect('equal', adjustable='box')
    plt.axis([-1, 3, -1.5, 1.5])
    # グラフをプロット
    plt.plot(x, y)
    plt.show()

interact(mathplot, time=(0, 2 * np.pi, 0.01))
