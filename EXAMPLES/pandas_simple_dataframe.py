#!/usr/bin/env python
'''

@author: jstrick
Created on Sun May 19 20:42:32 2013

'''
from pandas.core.frame import DataFrame
from printheader import print_header

cols = ['alpha','beta','gamma','delta','epsilon']
indices = ['a','b','c','d','e','f']
values = [
    [100, 110, 120, 130, 140],
    [200, 210, 220, 230, 240],
    [300, 310, 320, 330, 340],
    [400, 410, 420, 430, 440],
    [500, 510, 520, 530, 540],
    [600, 610, 620, 630, 640],
]
print_header('cols')
print(cols, '\n')

print_header('indices')
print(indices, '\n')

print_header('values')
print(values, '\n')

df = DataFrame(values, index=indices, columns=cols)
print_header('DataFrame df'),
print(df, '\n')

print_header("df['gamma']")
print(df['gamma'])
