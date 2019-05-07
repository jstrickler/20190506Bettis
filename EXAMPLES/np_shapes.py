#!/usr/bin/env python
import numpy as np

a1 = np.arange(15)
print("a1 shape",a1.shape)
print()

print(a1)
print()

a1.shape = 3,5
print(a1)
print()

a1.shape = 5,3
print(a1)
print()

print(a1.flatten())
print()

print(a1.transpose())
print("------------------")

a2 = np.arange(40)
a2.shape = 2,5,4

print(a2)
print()

print(a2.transpose())
print(a2.transpose().shape)
print()

a2.shape = 2,2,10
print(a2)
print()
