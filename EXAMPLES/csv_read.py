#!/usr/bin/env python
"""
csv_read.py

@author: jstrick
Created on Sun Mar 10 14:15:51 2013

"""
import csv

with open('../DATA/presidents.csv') as presidents_in:
    rdr = csv.reader(presidents_in)
    for row in rdr:
        print('{0:25s} {1:12s} {2}'.format(
            row[1],row[2], row[-1]
        ))
