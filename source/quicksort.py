# coding: utf-8
import numpy as np


def quicksort(x):
    if x == []:
        return []
    return(quicksort([a for a in x[1:] if a <= x[0]]) + [x[0]] + quicksort([a for a in x[1:] if a > x[0]]))

data = np.random.rand(10) * 100
print(data)
print(quicksort(data))
input()