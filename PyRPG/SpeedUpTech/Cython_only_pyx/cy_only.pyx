cimport numpy as np

def cy_algo(np.ndarray[long, ndim=1] arr_a, np.ndarray[long, ndim=1] arr_b):
    cdef long long res = 0
    cdef size_t len_a = len(arr_a)
    cdef size_t len_b = len(arr_b)

    for i in range(len_a):
        for j in range(len_b):
            res = res + arr_a[i] +arr_b[j]
    return res