#!/usr/bin/env python

import os

values = (5, 8, 17, 6, 5)
d1 = { v:v**2 for v in values }
print(d1)
print()

DIR = '../DATA/'
files = os.listdir(DIR)
file_sizes = { f:os.path.getsize(DIR + f) for f in files }
print(file_sizes)
print()
