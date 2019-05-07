#!/usr/bin/env python
from pprint import pprint



field_names = """term lastname firstname birthdate deathdate
birthplace birthstate termstart termend party""".split()

presidents = []

with open('DATA/presidents.txt') as pres_in:
    for raw_line in pres_in:
        fields = raw_line.rstrip().split(':')
        presidents.append(dict(zip(field_names, fields)))

pprint(presidents)
