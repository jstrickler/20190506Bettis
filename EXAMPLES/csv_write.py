#!/usr/bin/env python
"""

@author: jstrick
Created on Sun Mar 10 17:16:33 2013

"""
import csv

data = (
    ('February', 28, 'The shortest month, with 28 or 29 days'),
    ('March', 31, 'Goes out like a "lamb"'),
    ('April', 30, 'Its showers bring May flowers'),
)

with open('../TEMP/stuff.csv', 'w') as STUFF:
    wtr = csv.writer(STUFF)
    for row in data:
        wtr.writerow(row)
