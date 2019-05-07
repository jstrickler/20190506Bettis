#!/usr/bin/env python3

names = []
with open('../DATA/presidents.txt') as pres:
    for line in pres:
        flds = line[:-1].split(':')
        names.append(flds[2] + ' ' + flds[1])

upper_names = ( n.upper() for n in names )

for name in upper_names:
    print(name)
