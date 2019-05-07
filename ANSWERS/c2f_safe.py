#!/usr/bin/python3

import sys

try:
    c = float(input("Enter Celsius temp: "))
except ValueError as e:
    print("Error!",e)    
    sys.exit(1)

f = ((9 * c) / 5 ) + 32

print("{0:.1f} C is {1:.1f} F".format(c,f))

