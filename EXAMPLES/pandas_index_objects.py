#!/usr/bin/env python
from pandas.core.frame import Index, Series, DataFrame
from printheader import print_header

index1 = Index(['a','b','c'], name='letters')
index2 = Index(['b','a','c'])
index3 = Index(['b','c','d'])
index4 = Index(['red','blue','green'], name='colors')

print_header("index1, index2, index3", 70)
print(index1)
print(index2)
print(index3)
print()

print_header("index2 & index3", 70)
# these are the same
print(index2 & index3)
print(index2.intersection(index3))
print()

print_header("index2 | index3", 70)
# these are the same
print(index2 | index3)
print(index2.union(index3))
print()

print_header("index1.difference(index3)", 70)
print(index1.difference(index3))
print()

print_header("Series([10,20,30], index=index1)", 70)
series1 = Series([10,20,30], index=index1)
print(series1)
print()

print_header("DataFrame([(1,2,3),(4,5,6),(7,8,9)], index=index1, columns=index4)", 70)
dataframe1 = DataFrame([(1,2,3),(4,5,6),(7,8,9)], index=index1, columns=index4)
print(dataframe1)
print()

print_header("DataFrame([(1,2,3),(4,5,6),(7,8,9)], index=index4, columns=index1)", 70)
dataframe2 = DataFrame([(1,2,3),(4,5,6),(7,8,9)], index=index4, columns=index1)
print(dataframe2)
print()
