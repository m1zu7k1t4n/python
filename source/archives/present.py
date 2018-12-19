# coding: utf-8

import numpy as np

for zm in range(8):
    dataset = np.random.rand(10) * 100
    dataset = list(dataset)
    for i,v in enumerate(dataset):
        print(i,int(v))
    else:
        print()

    dataset.sort()
    for i,v in enumerate(dataset):
        print(i,int(v))

input()