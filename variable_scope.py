#!/usr/bin/env python

len = 33

toast = 100   # GLOBAL

x = [1, 2, 3]


def spam():
    jam = 'strawberry'  # LOCAL
    toast = 'sourdough' # LOCAL
    print("toast is", toast)
    print("in spam(): toast is", toast)
    print(len(x))


spam()

print("in main: toast is", toast)


