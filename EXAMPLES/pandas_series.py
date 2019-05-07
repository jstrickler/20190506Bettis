#!/usr/bin/env python
"""

@author: jstrick
Created on Sat May 18 10:46:25 2013

"""
import numpy as np
from pandas.core.frame import Series

NUM_VALUES = 10
index = [chr(i) for i in range(97,97 + NUM_VALUES)]
print(index)

s1 = Series(np.linspace(1,5,NUM_VALUES), index=index)
s2 = Series(np.linspace(1,5,NUM_VALUES))

print(s1, "\n")
print(s2, "\n")

print(s1[['h','b']], "\n")

print(s1[['a','b','c']], "\n")

print(s1.sum(), s1.mean(), s1.min(), s1.max(), "\n")
print(s1.cumsum(), s1.cumprod(), "\n")
print('a' in s1)
print('m' in s1)

s3 = s1 * 10
print(s3, "\n")

print(s3 > 25, "\n")
s3[s3 < 25] = -1
print(s3, "\n")


s4 = Series([-0.204708, 0.478943, -0.519439])
print(s4.max(), s4.min(), s4.max() - s4.min())


from pandas.core.frame import Series
s = Series([5,10,15], ['a','b','c'])
print(s)