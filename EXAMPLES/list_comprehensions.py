#!/usr/bin/python

fruits = ['watermelon','apple','mango','kiwi','apricot','lemon','guava']

values = [ 2, 42, 18, 92, "boom", ['a','b','c'] ]

ufruits = [ fruit.upper() for fruit in fruits ]

afruits = [ fruit for fruit in fruits if fruit.startswith('a') ]

doubles = [ v * 2 for v in values ]


print("ufruits:"," ".join(ufruits))
print("afruits:"," ".join(afruits))
print("doubles:", end=' ')
for d in doubles:
    print(d, end=' ')
print()

