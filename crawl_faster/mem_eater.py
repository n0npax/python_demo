@profile
def test():
    a = fun_a()
    b = a[:]+"_copy"
    a = "llama"
    del b
    b = "mouse"

def fun_a():
    return "a"*(10**8)

test()
