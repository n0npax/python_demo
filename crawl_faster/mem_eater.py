@profile
def test():
    a = fun_a()
    b = a[:] + "_copy"
    a = "llama"
    del b
    b = "mouse"
    return a, b


def fun_a():
    return "a" * (10 ** 8)


test()
