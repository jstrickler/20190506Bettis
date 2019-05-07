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





people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT' '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', "Seahawks", '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
]

first_name, last_name, *product, birth_date = people[0]
print(first_name, last_name, '\n')

for first_name, last_name, *product, birth_date in people:
    print(first_name, last_name, product, birth_date)
print()

colors = ['blue', 'purple', 'pink']
for i, color in enumerate(colors):
    print(i, color)
print(list(enumerate(colors)))

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

for abbr, name in airports.items():
    print(abbr, name)

print(airports.items())


words = [('Big', 'Deal'), ('So', 'What'), ("I'm", "Unimpressed")]

for w1, w2 in words:
    print(f"{w1} {w2}")


values = ['a', 'b', 'c', 'd', 'e', 'f']

x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)


colors = 'blue', 'purple', 'pink'
for x, *y in colors:
    print(x, y)


s = "wombat"

for i, c in enumerate(s):
    print(i, c)



