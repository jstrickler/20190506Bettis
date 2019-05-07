#!/usr/bin/env python
"""

@author: jstrick
Created on Sat May 18 16:20:49 2013

"""
from pandas.core.frame import Series

# create from list
s1 = Series([5,10,15])
print(s1, "\n")
print("s1[0]:",s1[0], "\n")
print('-' * 60)

# create from list with index
s2 = Series([5,10,15], ['a','b','c'])
print(s2, "\n")
print("s2['a']:", s2['a'])
print('-' * 60)

# create from dictionary (keys are indices)
s3 = Series({'b':10, 'a':5, 'c':15})
print(s3, "\n")
print("s3.sum(), s3.mean():", s3.sum(), s3.mean())
print('-' * 60)


