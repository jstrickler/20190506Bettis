#!/usr/bin/python3
colors = [ 'red', 'green', 'blue', 'purple', 'pink', 'yellow', 'black' ]

for color in colors:
    print(color)
print()

with open('../DATA/mary.txt') as MARY:
    for line in MARY:
        print(line,end='')
print()

while True:
    name = input("What is your name? ")
    if name.lower() == 'q':
       break
    print("Welcome,",name)