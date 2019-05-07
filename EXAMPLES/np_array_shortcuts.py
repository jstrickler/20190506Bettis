#!/usr/bin/env python
import numpy as np

a1 = np.r_[1, 2, 3]
print(a1)
print()

a2 = np.r_[1:20:2]
print(a2)
print()

a3 = np.r_[-1:1:10j]
print(a3)
print()

a4 = np.r_[a1, a2, a3]
print(a4)
print()

a5 = np.r_['2', [1,2,3], [4,5,6]]
print(a5)
print()


exit(1)

a6 = np.r_['1,2,0', [1,2,3], [4,5,6]]
print(a6)
print()

m = np.r_['r',[1,2,3], [4,5,6]]
print(m)
print(type(m))

