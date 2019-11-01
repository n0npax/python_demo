from math import log
import math
import dis_func_cyth

mylog1c = dis_func_cyth.mylog1c
mylog2c = dis_func_cyth.mylog2c


def mylog1p():
    return sum([log(i) for i in range(1, 1000)])


def mylog2p():
    return sum([math.log(i) for i in range(1, 1000)])


def mylog3p(log=math.log):
    return sum([log(i) for i in range(1, 1000)])


#%timeit mylogX

import timeit

for f in [mylog1p, mylog2p, mylog3p, mylog1c, mylog2c]:
    t = timeit.timeit(
        f"{f.__name__}()",
        setup=f"from __main__ import log, math, {f.__name__}",
        number=10000,
    )
    print(f"{f.__name__} -> {f()} {t}")
