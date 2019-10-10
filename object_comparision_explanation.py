class A:
    def __init__(self): print("init")
    def __del__(self): print("delete")

print("A() is A()")
print(">>",A() is A())
print("")
print("id(A()) == id(A())")
print(">>",id(A()) == id(A()))
