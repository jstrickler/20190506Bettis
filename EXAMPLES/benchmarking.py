#!/usr/bin/env python
# (c)2015 John Strickler

import timeit

setup = '''
from datetime import datetime, date
date_strings = '1952-09-22', '1956-10-31', '1990-08-27', '2014-08-01'
date_fmt = '%Y-%m-%d'
'''

test1 = '''
for date_string in date_strings:
    t = datetime.strptime(date_string, date_fmt).date()
'''

test2 = '''
for date_string in date_strings:
    year, month, day = date_string.split('-')
    t = date(int(year), int(month), int(day))
'''

timer1 = timeit.Timer(test1, setup)
print("test 1:", timer1.timeit())

timer2 = timeit.Timer(test2, setup)
print("test 2:", timer2.timeit())

