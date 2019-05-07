#!/usr/bin/env python

try:
    x = 5
    y = "cheese"
    z = x + y
    print("Bottom of try")

except TypeError as err:
    print("Naughty programmer! ", err)

print("After try-except")
