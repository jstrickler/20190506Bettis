#!/usr/bin/python

import csv

with open('../DATA/presidents.csv') as pres_in:
    rdr = csv.reader(pres_in)
    for row in rdr:
        full_name = row[2] + ' ' + row[1]
        state = row[4]
        print(('{0:40s} {1:30s}'.format(full_name,state)))
