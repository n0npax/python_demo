from math import log
import math


def mylog1():
    return sum([log(i) for i in range(1, 1000)])


def mylog2():
    return sum([math.log(i) for i in range(1, 1000)])


def mylog3(log=math.log):
    return sum([log(i) for i in range(1, 1000)])


#%timeit mylogX

assert mylog2() == mylog3() == mylog1()

import timeit

print(
    f'mylog1() -> {timeit.timeit("mylog1()", setup="from __main__ import log, math, mylog1")}'
)
print(
    f'mylog2() -> {timeit.timeit("mylog2()", setup="from __main__ import log, math, mylog2")}'
)
print(
    f'mylog3() -> {timeit.timeit("mylog3()", setup="from __main__ import log, math, mylog3")}'
)
