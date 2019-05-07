#!/usr/bin/env python
"""

@author: jstrick
Created on Mon May 27 22:32:20 2013

"""
import numpy as np
from pandas.core.frame import DataFrame
from printheader import print_header

dataset1 = np.arange(9.).reshape((3,3))

df1 = DataFrame(
    dataset1,
    columns = ['apple', 'banana', 'mango'],
    index = ['orange', 'purple', 'blue']
)

dataset2 = np.arange(12.).reshape((4,3))

df2 = DataFrame(
    dataset2,
    columns = ['apple', 'banana', 'kiwi'],
    index = ['orange', 'purple', 'blue', 'brown']
)

print_header('df1')
print(df1)
print()

print_header('df2')
print(df2)
print()

print_header('df1 + df2')
print(df1 + df2)

print_header('df1.add(df2, fill_value=0)')
print(df1.add(df2, fill_value=0))
