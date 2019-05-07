#!/usr/bin/python

fruits = ['watermelon', 'apple', 'kiwi', 'lime', 'orange', 'cherry',
'banana', 'raspberry', 'grape', 'lemon', 'durian', 'guava', 'mango',
'papaya', 'mangosteen', 'breadfruit']

s = slice(5)  # first 5 
print(fruits[s])
print()

s = slice(-5,None)  # last 5
print(fruits[s])
print()

s = slice(3,8)  #  4th through 8th
print(fruits[s])
print()

s = slice(None,None,2) # every other fruit starting with element 0
print("slice(None,None,2)", fruits[s])
print('-' * 50)

seq = ('red', 5, 'blue', 3, 'yellow', 7, 'purple', 2, 'pink', 8)
key_slice = slice(None,None,2)  #  even elements
print("keys:", seq[key_slice])
value_slice = slice(1,None,2)   #  odd elements
print("values:", seq[value_slice])
kv_tuples = list(zip(seq[key_slice], seq[value_slice]))  # generates key/value pairs as tuples
color_dict = dict(kv_tuples)   # initialize a dictionary from key/value pairs
print("color_dict:", color_dict)
