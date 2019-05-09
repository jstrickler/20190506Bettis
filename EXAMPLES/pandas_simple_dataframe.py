#!/usr/bin/env python
'''

@author: jstrick
Created on Sun May 19 20:42:32 2013

'''
from pandas import DataFrame
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

print(df['gamma']['a'])
print(df.loc['a', 'gamma'])

df['eta'] = df['alpha'] + df['beta']

df.insert(2, 'rho', df['gamma'] * df['delta'])

print(df)

print(df.columns)
print(cols)


df.loc['h'] = range(7)

print(df)


df.loc['g'] = range(9, 16)
print(df)

# DF.loc[ROW-SPEC, COLUMN-SPEC]

df.loc[:, :] = 42

print(df)
