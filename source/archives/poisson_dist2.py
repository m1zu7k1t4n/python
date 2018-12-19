# -*- coding: utf-8 -*-
import math, random
import numpy as np
from pylab import *
from scipy.stats import poisson
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()

tmp = range(1, 700)
lambda_list = list(map(lambda x: x*0.1, tmp))

frame_list = []

x = np.arange(16)

for lamda in lambda_list:
    one_frame = plt.bar(x, poisson.pmf(x, lamda))
    frame_list.append(one_frame)

ani = animation.ArtistAnimation(fig, frame_list, interval = 40, repeat_delay = 20)
plt.show()