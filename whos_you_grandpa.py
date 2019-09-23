from dataclasses import dataclass

@dataclass
class A:
    x: int = 1

@dataclass
class B:
    x: int = 2

class C(A,B):
    pass

c = C()
print(c.x)
