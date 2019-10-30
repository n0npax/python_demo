import math

def test():
    s = 0
    for i in range(10**7):
         s+=math.sin(i)
    return s

test()
