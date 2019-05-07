#!/usr/bin/env python
import numpy as np

a = np.array(
[[70, 31, 21, 76, 19, 5, 54, 66],
 [23, 29, 71, 12, 27, 74, 65, 73],
 [11, 84, 7, 10, 31, 50, 11, 98],
 [25, 13, 43, 1, 31, 52, 41, 90],
 [75, 37, 11, 62, 35, 76, 38, 4]]
)

print('a =>', a)
print()

i = a > 50
print('i (a > 50) =>', i)
print()

print('a[i] =>', a[i])
print(a[a > 50])
print()
print('a[i].min(), a[i].max() =>', a[i].min(), a[i].max())
print()
a2 = np.copy(a)
a2[i] = 0
print('a2 =>', a2)
print()

a[a < 15] += 10
print(a)
