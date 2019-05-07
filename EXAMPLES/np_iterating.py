#!/usr/bin/env python
import numpy as np

a = np.array(
[[70, 31, 21, 76, 19, 5, 54, 66],
 [23, 29, 71, 12, 27, 74, 65, 73]]
)

b = np.array(
[[11, 84, 7, 10, 31, 50, 11, 98],
 [25, 13, 43, 1, 31, 52, 41, 90]]
)
print('a =>\n', a)
print()

print('b =>\n', b)
print()

print("for row in a: =>")
for row in a:
    print("row:", row)
print()

print("for elem in a.flat: =>")
for elem in a.flat:
    print("element:", elem)