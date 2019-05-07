#!/usr/bin/env python

num_pairs = [ (5.0, 1), (1.0, 5), (5.0, 0), (0, 5.0) ]

total = 0

for x, y in num_pairs:
    try:
        quotient = x/y
    except Exception as e:
        print("Error when y = {0}, {1}".format(y, e))
    else: 
        total += quotient
        print(total)
