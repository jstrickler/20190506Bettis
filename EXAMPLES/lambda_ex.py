#!/usr/bin/python

fruits = ['watermelon','Apple','Mango','KIWI','apricot','LEMON','guava']

sorted_fruits = sorted(fruits,key=lambda e: e.lower())

print(" ".join(sorted_fruits))

