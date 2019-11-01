# cython: language_level=3
cimport cython
from libc.stdlib cimport malloc, free

from math import log

import array

def mylog1c(log=log):
    return sum([log(i) for i in range(1, 1000)])

def mylog2c():
    cdef int i = 1
    cdef double s = 0.0
    while i < 1000:
        s += log(i)
        i += 1
    return s
