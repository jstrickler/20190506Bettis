#!/usr/bin/env python

import scipy as sp

# 2,1,4 are coefficients
p1 = sp.poly1d([2, 1, 4])
print(p1)
print()
# evaluate for x = .75
print(p1(.75))
# get the roots
print(p1.r)
print()

# 2,1,4 are roots
p2 = sp.poly1d([2, 1, -4], True)
print(p2)
print()
# evaluate for x = .75
print(p2(.75))
# get the roots
print(p2.r)
print()


# 1,2,3 are coefficients, variable is 'm'
p3 = sp.poly1d([1, 2, 3], False, 'm')
print(p3)
print()
# evaluate for m = 100
print(p3(100))
# get the roots
print(p3.r)
print()

# polynomial arithmetic
p4 = sp.poly1d([1,2])
p5 = sp.poly1d([3,4])
print()
print(p4)
print()
print(p5)
print()
print(p4 + p5)
print()
print(p4 - p5)
print()
print(p4 ** 3)
print()