# coding: utf-8
import matplotlib.pyplot as plt
import numpy.random as npr
import numpy as np
from math import sin, pi
np.set_printoptions(threshold=np.inf)

a = npr.rand()
b = npr.rand(100)  # 乱数を100個生成
c = npr.rand(100, 100)

d = npr.rand(100) * 40 + 30  # 30~70の乱数を100個生成

""" 標準正規分布。いわゆるガウシアン。標準正規分布ならば randn() で、平均・分散を指定したい場合は normal() を用いる。"""
e = npr.randn()         # 標準正規分布 (平均0, 標準偏差1)
f = npr.randn(100) + 50      # 標準正規分布を10個生成
g = npr.randn(10, 10)    # 標準正規分布による 10x10 の行列
h = npr.normal(50, 10)   # 平均50、標準偏差10の正規分布
i = npr.beta(a=3, b=5)

city = ["Sapporo", "Sendai", "Tokyo", "Nagoya", "Kyoto", "Osaka", "Fukuoka"]

j = npr.choice(city)                     # 1個をランダム抽出
k = npr.choice(city, 10)                  # 10個をランダム抽出（重複あり）
l = npr.choice(city, 5, replace=False)  # 5個をランダム抽出（重複なし)

m = npr.randint(100)  # 0~99の整数を1つ生成
n = npr.randint(0, 100, 10)  # 0~99の整数を20つ生成

weight = [0.1, 0.1, 0.3, 0.1, 0.1, 0.2, 0.1]
m = npr.choice(city, 10, p=weight)

R = npr.randn(1000)
plt.hist(R, bins=100)
plt.show()

L = 10000                            # 歩数
M = [-1, 1]
step = npr.choice(M, L)      # +1 or -1 をL個生成
position = np.cumsum(step)             # 位置の変化
plt.plot(position)
plt.show()
print(np.sum(step))
print(np.sum(position))
