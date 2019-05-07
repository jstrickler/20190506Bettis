#!/usr/bin/env python
from pprint import pprint

with open('DATA/knights.txt') as knights_in:
    lines = (line.rstrip().split(':') for line in knights_in)
    knight_info = {line.pop(0):line for line in lines }


pprint(knight_info)
print()

#  {K:V for VAR in ITERABLE if COND}


airports = {
    'EWR': 'Newark',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SAC': 'Sacramento',
    'IAD': 'Dulles',
}

sa = {k:v for k, v in sorted(airports.items())}

pprint(sa)
print()

sa = dict(sorted(airports.items()))

pprint(sa)
print()

food = ['SPam', 'spam', 'SPAM', 'eggs', 'Eggs', 'SPaM', 'EggS', 'Spam', 'Spam',
        'EGGS', 'spam', 'spam', 'eggs']

unique_foods = set(f.lower() for f in food)  # set comprehension
unique_foods = {f.lower() for f in food} # set comprehension

print(unique_foods)








