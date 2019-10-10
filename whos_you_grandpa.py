#!/usr/bin/env python3.8

from dataclasses import dataclass


@dataclass
class A:
    x: str = "A"


@dataclass
class B:
    x: str = "B"


class C(A, B):
    pass


c = C()
print(c.x)
