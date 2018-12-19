import functools
import time
import numpy as np
from numba import jit

def timer(name):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print("%s watch start" % name)
            timestart = time.time()
            func(*args, ** kwargs)
            timestop = time.time() - timestart
            print("time:%03.5f" % timestop)
        return wrapper
    return decorator

num = 1000000


# @timer("append")
def appb(n):
    xs = []
    for i in range(n):
        xs.append(i)


@timer("for")
def forb(n):
    xs = [i for i in range(n)]


@timer("None")
def Noneb(n):
    xs = [None] * n
    for i in range(n):
        xs[i]


@timer("Noneonly")
def Noneonlyb(n):
    xs = [None] * n


@timer("zero")
def zerob(n):
    xs = [0] * n


@timer("array")
def arrayb(n):
    xs = np.array([0 for _ in range(n)])


@timer("narray")
def narrayb(n):
    xs = np.array([i for i in range(n)])

# @timer("append")
# @jit
# def appb(n):
#     xs = []
#     for i in range(n):
#         xs.append(i)


# @timer("for")
# @jit
# def forb(n):
#     xs = [i for i in range(n)]


# @timer("None")
# @jit
# def Noneb(n):
#     xs = [None] * n
#     for i in range(n):
#         xs[i]


# @timer("Noneonly")
# @jit
# def Noneonlyb(n):
#     xs = [None] * n


# @timer("zero")
# @jit
# def zerob(n):
#     xs = [0] * n


# @timer("array")
# @jit
# def arrayb(n):
#     xs = np.array([0 for _ in range(n)])


# @timer("narray")
# @jit
# def narrayb(n):
#     xs = np.array([i for i in range(n)])


appb(num)
forb(num)
Noneb(num)
Noneonlyb(num)
zerob(num)
arrayb(num)
narrayb(num)
