#!/usr/bin/env python

def greet(greeting, whom):
    print(f"{greeting} {whom}")

greet("Hi", "Mom")
print()

greetings = [
    ("Hi", "Mom"),
    ("Yo", "Dog"),
    ("'Sup", "Bro"),
    ("Hello", "Newman"),
]

for g in greetings:
    greet(*g)

x = ['Vale', 'Caesar']

greet(*x)

