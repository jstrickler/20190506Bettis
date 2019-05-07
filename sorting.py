#!/usr/bin/env python

nums = [800, 80, 1000, 32, 255, 400, 5, 5000]

n1 = sorted(nums)
print("n1:", n1, "\n")

n2 = sorted(nums, reverse=True)
print("n2:", n2, "\n")

fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f1 = sorted(fruits)
print("f1:", f1, '\n')

def ignore_case(s):
    return s.lower()

#                       KEY FUNCTION (convert item to comparison value)
f2 = sorted(fruits, key=ignore_case)
print("f2:", f2, '\n')

f3 = sorted(fruits, key=len)
print("f3:", f3, '\n')

def custom_sort(fruit):
    return len(fruit), fruit.lower()

f4 = sorted(fruits, key=custom_sort)
print("f4:", f4, '\n')

f5 = sorted(fruits, key=str.lower)
print("f5:", f5, '\n')

def wacky(s):
    return s[-1]

f6 = sorted(fruits, key=wacky)
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


def by_last_name(p):
    return p[1], p[0]


for first_name, last_name, _, birth_date in sorted(people, key=by_last_name):
    print(first_name, last_name, birth_date)


things = [5, 'a', 10, 2, 'm', 'c', 0, 'x']

# t1 = sorted(things)
t1 = sorted(things, key=str)
print("t1:", t1, '\n')

def magic(x):
    if isinstance(x, str):
        return 10000000000, x
    else:
        return x, ''

t1 = sorted(things, key=magic)
print("t1:", t1, '\n')


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

#  lambda param ...: return_value

for abbr, name in sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(abbr, name)
print()

def by_value(e):
    return e[1], e[1]

for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print()

counts = {}

with open('DATA/words.txt') as words_in:
    for raw_line in words_in:
        first_letter = raw_line[0]

        counts[first_letter] = counts.get(first_letter, 0) + 1

print(counts)

for letter, count in sorted(counts.items(), key=lambda e: e[1], reverse=True):
    print(letter, count)






