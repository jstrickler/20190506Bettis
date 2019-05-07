#!/usr/bin/env python
import sys
from copy import deepcopy

print("Hello, world")

x = 10

actor = 'Chris Hemsworth'

x = 5.4

y = x

# int x = 5;   NOT IN PYTHON

print(x * y)

# print(actor + x)

print(actor * 10)

#   SEQ * INT

#    prime_factor = get_prime_factor(...)

#  a-z A-Z _ 0-9

_ = 5

print(_)

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r'spam\n'

print("Guido's the man")
print('Guido "BDFL" is aweome')

print("""Guido's the "main" man!""")

actor = "Chris Hemsworth"
city = "Malibu"

print(f"{actor} lives in {city}")
print("{} lives in {}".format(actor, city))

print(f"2 + 2 is {2 + 2}")

result = 23.1 / 19.7

print(f"result is {result:.3f}")

print(actor.upper())
print(actor.count('h'))
print(actor.lower().count('h'))

print(len(actor))

cities = ['Pittsburgh', 'Ohiopyle', 'Altoona', 'Sewickley',
          'Beaver Falls']

print(cities[0], cities[-1])
print(cities[0], cities[-1], sep=',')
print(cities[0], cities[-1], sep='')
print(cities[0], cities[-1], end='\n\n')

cities.append('Rochester')

more_cities = ['Greensburg', 'Aliquippa', 'Harrisburg', 'Philadelphia']

# print(a, b, c)

cities.extend(more_cities)

print(cities)


values = ['a', 'b', 'c']

x = ['d', 'e', 'f']

print(values)
# values.append(x)
values.extend(x)
print(values)

print('/'.join(values))

delim = ', '

print(delim.join(values))

print(values, file=sys.stderr)

# print(...., file=sys.stdout, sep=' ', end='\n', flush=False)


x = "12,233,....,.."

print(x.rstrip('.,'))

y = 'xxxxABC'
print(y.lstrip('x'))

z = 'xxxxABCyyyy'

print(z.strip('xy'))

s1 = '     PA PA PA      '

print(s1.strip())

print(s1.replace(' ', ''))


print(cities)


even_more_cities = ['Monroeville', 'Confluence', 'Reading']

cities[2:4] = even_more_cities

print(cities)

actor = "Chris Hemsworth"

print(actor[0], actor[9], actor[-1])

print(actor[0:4])

print(actor[6:9])

#   SEQ[START:STOP]   SEQ[START:STOP:STEP]
#   SEQ[START:]  SEQ[:STOP]  SEQ[:]

print(actor[-5:])



values = ['a', 'b', 'c']

vcopy = values

vcopy.append('wombat')

print(values)

vcopy2 = list(values)
vcopy3 = values[:]

vcopy3.append('platypus')

print(values)


spam = [['a', 'b', 'c'], [1, 2, 3]]

ham = list(spam)

eggs = spam

print(id(spam), id(ham), id(eggs))

ham[0].append("wow")

print(spam)

toast = deepcopy(spam)

toast[1].append("walrus")
print(toast)
print(spam)



a = "Bob"
b = a

a = "Fred"

print(a, b)

m = [1, 2, 3]

n = m

n.append(5)

































