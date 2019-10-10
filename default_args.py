def f(x=4, a=[]):
    a.append(x)
    print(a)


f()
f(2)
f(7, [7, 7])
f("still")
