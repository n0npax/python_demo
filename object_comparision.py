'''6.10.3. Identity comparisons
The operators is and is not test for an object’s identity: x is y is true if and only if x and y are the same object. An Object’s identity is determined using the id() function. x is not y yields the inverse truth value. '''
# Ref: https://docs.python.org/3/reference/expressions.html#is

class A: pass

print(A() is A())
print(id(A()) == id(A()))
