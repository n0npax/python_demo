class A:
    def __init__(self): print("init")
    def __del__(self): print("delete")

print("compare obj")
print(A() == A())
print("compare ids")
print(id(A()) == id(A()))
