#!/usr/bin/env python

person = 'Bill', 'Gates', 'Microsoft'

location = 78, -35

months = 'Jan', 'Feb', 'Mar',  # ...

singleton = 5,

thing = "wombat",

other_thing = ()   # empty tuple

first_name, last_name, product = person

# x = first_name, last_name, product

# no use case for this, usually
for x in person:
    print(x)




values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values



