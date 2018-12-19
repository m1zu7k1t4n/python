# -*- coding: utf-8 -*-
import numpy as np
import math as m
import sympy as sp
NUM = int(input())
time = [int(input()) for _ in range(NUM)]
time.sort()
tmp = time[0]
for i in range(1,len(time)):
    tmp = sp.lcm(tmp, time[i])
time_max = tmp
result = 0

for num in time[:]:
    rest = 10000000
    count = 1
    rest_before = 1000000
    while rest >= 0:
        rest_before = rest
        rest = (time_max // count) - num
        count += 1
    result += rest_before
print(result)