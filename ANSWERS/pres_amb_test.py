#!/usr/bin/env python
# (c)2014 John Strickler
#
from .pres_amb import get_info, get_oldest, get_youngest

print('PRESIDENT 1:')
for k,v in list(get_info(1).items()):
    print((k,v))
print()
print('PRESIDENT 44:')
for k,v in list(get_info(44).items()):
    print((k,v))
print()

oldster = get_oldest()
print(("Oldest is",oldster["firstname"],oldster["lastname"]))

youngster = get_youngest()
print(("Youngest is",youngster["firstname"],youngster["lastname"]))
