#!/usr/bin/python
from datetime import date

date_tuples = [
    (1968, 10, 11),
    (1968, 12, 21),
    (1969, 3, 3),
    (1969, 5, 18),
    (1969, 7, 16),
    (1969, 11, 14),
    (1970, 4, 11),
    (1971, 1, 31),
    (1971, 7, 26),
    (1972, 4, 16),
    (1927, 12, 7),
]

for dt in date_tuples:
    d = date(*dt)  # instead of date(dt[0], dt[1], dt[2])
    print(d)