#!/usr/bin/env python
# (c)2014 John Strickler
#
from .pres import get_info

print('PRESIDENT 1:')
for field, value in list(get_info(1).items()):
    print((field, value))
print()

print('PRESIDENT 44:')
for field, value in list(get_info(44).items()):
    print((field, value))
