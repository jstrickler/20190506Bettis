#!/usr/bin/env python
# (c)2015 John Strickler

values = ['a', 'b', 'c', 'd', 'e']

x, y, *z = values
print("x: {}    y: {}    z: {}".format(x, y, z))
print()

x, *y, z = values
print("x: {}    y: {}    z: {}".format(x, y, z))
print()

*x, y, z = values
print("x: {}    y: {}    z: {}".format(x, y, z))
print()

people = [
    ('Bill', 'Gates', 'Microsoft'),
    ('Steve', 'Jobs', 'Apple'),
    ('Paul', 'Allen', 'Microsoft'),
    ('Larry', 'Ellison', 'Oracle'),
    ('Mark', 'Zuckerberg', 'Facebook'),
    ('Sergey','Brin', 'Google'),
    ('Larry', 'Page', 'Google'),
    ('Linux', 'Torvalds', 'Linux'),
]

for *name, _ in people:
    print(name)
print()
