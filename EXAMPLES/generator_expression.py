#!/usr/bin/python
import re

# sum the squares of a list of numbers
# using list comprehension, entire list is stored in memory
s1 = sum([x*x for x in range(10)])
# only one square is in memory at a time with generator expression 
s2 = sum(x*x for x in range(10))
print(s1,s2)
print()

# set constructor -- does not put all words in memory
pg = open("../DATA/mary.txt")
s = set(word.lower()  for line in pg  for word in re.split(r'\W+',line))
pg.close()
print(s)
print()

keylist = ['OWL','Badger','bushbaby','Tiger','GORILLA','AARDVARK']
# dictionary constructor
d = dict( (k.lower(),k) for k in keylist)
print(d)
print()

#
with open("../DATA/mary.txt") as M:
    max_line_len = max(len(line)  for line in M if line.strip())

print("Max line len:", max_line_len)
2
