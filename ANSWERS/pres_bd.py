#!/usr/bin/env python

name_slice = slice(1,3)
bd_slice = slice(3,6)

with open('../DATA/presidents.txt') as PRES:
    for line in PRES:
        flds = line.split(':')
        names = flds[name_slice]
        bd = flds[bd_slice]
        print(("{0[1]} {0[0]}: {1[1]} {1[2]}, {1[0]}".format(names, bd)))