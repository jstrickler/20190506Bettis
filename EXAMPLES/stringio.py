#!/usr/bin/env

from io import StringIO as sio

mary = sio(
'''Mary had a little lamb;
Its fleece was white as snow;
And everywhere that Mary went
The lamb was sure to go.
'''
)

for line in mary:
    print(line, end='')
