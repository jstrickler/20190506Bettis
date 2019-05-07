#!/usr/bin/env python

value = 56

if value > 75:
    print('platypus')
elif value > 50:
    print('wombat')
    print('crocodile')
elif value > 25:
    print("kookaburra")
else:
    print("drop bear")

print("Done.")

class IsOdd:
    def __init__(self, value):
        self._value = value


    def __bool__(self):
        return bool(self._value % 2)

    def __len__(self):
        return 42


a = IsOdd(1)
b = IsOdd(2)
c = IsOdd(14)

print(bool(a), bool(b), bool(c))

print(len(a))

#  == != > < >= <=

#  is

#  if x is None:
#     ....


debug = False


display_text("Look out!", 'red' if debug else 'blue')

#    debug?'red':'blue'












