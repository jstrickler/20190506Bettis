#!/usr/bin/env python
"""

@author: jstrick
Created on Sun Jun  9 21:36:10 2013

"""
from pandas.core.frame import DataFrame
from printheader import print_header

cols = ['alpha','beta','gamma','delta','epsilon']
index = ['a','b','c','d','e','f']
values = [
    [100, 110, 120, 130, 140],
    [200, 210, 220, 230, 240],
    [300, 310, 320, 330, 340],
    [400, 410, 420, 430, 440],
    [500, 510, 520, 530, 540],
    [600, 610, 620, 630, 640],
]

df = DataFrame(values, index=index, columns=cols)
print_header('DataFrame df')
print(df, '\n')

# select a column
print_header("df['alpha']:")
print(df['alpha'], '\n')

# same as above
print_header("df.alpha:")
print(df.alpha, '\n')

# slice rows
print_header("df['b':'e']")
print(df['b':'e'], '\n')

# slice columns
print_header("df[['alpha','epsilon','beta']]")
print(df[['alpha','epsilon','beta']])
print()



