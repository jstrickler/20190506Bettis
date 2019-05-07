#!/usr/bin/python3

import sys

temp_str = input("Enter Celsius temp: ") 
c = float(temp_str)
f = ((9 * c) / 5 ) + 32

print("{0:.1f} C is {1:.1f} F".format(c,f))

