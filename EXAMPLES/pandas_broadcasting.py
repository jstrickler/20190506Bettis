#!/usr/bin/env python
"""

@author: jstrick
Created on Tue Jun  4 21:55:55 2013

"""
import pandas as pd
from pandas import DataFrame, Series
from printheader import print_header

cols = ['alpha','beta','gamma','delta','epsilon']
index = pd.date_range('2013-01-01 00:00:00',periods=6, freq='D')

print(index, "\n")

values = [
    [100, 110, 120, 930, 140],
    [250, 210, 120, 130, 840],
    [300, 310, 520, 430, 340],
    [275, 410, 420, 330, 777],
    [300, 510, 120, 730, 540],
    [150, 610, 320, 690, 640],
]

ser1 = Series([.1, .2, .3, .4, .5])

df = DataFrame(values, index, cols)
print_header("Basic DataFrame:")
print(df)
print()




print_header("Triple each column")
print(df * 3)
print()

print_header("Multiply column gamma by 1.5")
df['gamma'] *= 1.5
print(df)
print()

print_header("Multiply by strings")
df['gamma'] *= 'spam'
print(df)
print()
