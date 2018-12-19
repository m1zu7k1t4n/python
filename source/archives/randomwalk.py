# -*- coding: utf-8 -*-
import numpy.random as npr
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

np.set_printoptions(threshold=np.inf)
# ランダムウォークのグラフ化
L = 1000  # 歩数
M = [1, -1]
# weight = [,,] choice(M, L, p=weight)
step = npr.choice(M, L)  # +1 or -1 をL個生成
position = np.cumsum(step)  # 位置の変化
plt.plot(position)
plt.show()
# plt.savefig("great.png")

"""
L = 1000000
M = [i for i in range(1000)]
step = npr.choice(M, L)
step.sort()
counter = Counter(step)
print(counter)
print(sum(step) / len(step))
plt.plot(step)
plt.show()
"""
