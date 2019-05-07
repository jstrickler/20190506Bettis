#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0, '\n')

f1 = [f.upper() for f in fruits]
print("f1:", f1, '\n')

# [EXPR for VAR ... in ITERABLE if COND ...]

f2 = [f.upper() for f in fruits if f.startswith('p')]
print("f2:", f2, '\n')

f3 = [f.upper() if f.startswith('p') else f for f in fruits]
print("f3:", f3, '\n')

f4 = []
for f in fruits:
    if f.startswith('p'):
        f4.append(f.upper())
    else:
        f4.append(f)
print("f4:", f4, '\n')


def make_p_upper(x):
    if x.lower().startswith('p'):
        return x.upper()
    return x

f5 = [make_p_upper(f) for f in fruits]
print("f5:", f5, '\n')

f6 = [f.capitalize() if f[0].lower() in 'aeiou' else f for f in fruits]
print("f6:", f6, '\n')


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = sorted(set([p[1].upper() for p in people]))
print(last_names, '\n')

last_name_gen = (p[1].upper() for p in people)

del people[5]

print(last_name_gen)
for last_name in last_name_gen:
    print(last_name)
print()

fruit_gen = (
    f.upper()
    for f in fruits
    if f.startswith('p')
)

for f in fruit_gen:
    print(f)
print()

def upper_fruit(fruitlist):
    for f in fruitlist:
        if f.startswith('a'):
            yield f.upper()


g = upper_fruit(fruits)

for fruit in g:
    # next(g)
    # next(g)
    # ...
    print(fruit)


def open(file_name):
    with __builtins__.open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip('\n\r')

mary_in = open('DATA/mary.txt')

for line in mary_in:
    print(line)

print('\n')

for line in mary_in:
    print(line)

















