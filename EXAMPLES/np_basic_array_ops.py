#!/usr/bin/env python
import numpy as np

a = np.array(
    [
        [ 5, 10, 15 ],
        [ 2,  4, 6  ],
        [ 3,  6, 9, ],
    ]
)

b = np.array (
    [
        [ 10, 85, 92 ],
        [ 77, 16, 14 ],
        [ 19, 52, 23 ],
    ]
)
print("a")
print(a)
print()
print("b")
print(b)
print()


print("a * 10")
print(a * 10)
print()

print("a + b")
print(a + b)
print()

print("b + 3")
print(b + 3)
print()

s1 = a.sum()
s2 = b.sum()
print("sum of a is {0}; sum of b is {1}".format(s1,s2))
print()

a += 1000
print(a)
