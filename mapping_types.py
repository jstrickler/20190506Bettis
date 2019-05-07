#!/usr/bin/env python
"""
Outstanding demo script for Bettis labs.
"""

# import ...
# from ... import ...

MAX_VALUES = 10


def main():
    """
    Program entry point.

    :return: None
    """
    dictionary_examples()
    set_examples()
    finding_unique_values()

def dictionary_examples():
    """
    How to use the dictionary.

    :return: None
    """
    d1 = dict()

    d2 = {'a': 5, 'm': 19, 'c': 12}

    d3 = {}

    d2['e'] = 5

    print(d2)

    print(d2['m'], '\n')

    for x in 'a', 'm', 'd', 'b', 'c':
        print(x, d2.get(x, 'NOT FOUND'))
    print()

    for x in 'a', 'm', 'd', 'b', 'c':
        print(x, d2.setdefault(x, 0))
    print()

    print(d2, '\n')


    for k, v in d2.items():
        print(k, v)
    print()

    for k, v in sorted(d2.items()):
        print(k, v)
    print()


def set_examples():
    """
    Excellent set examples

    :return: None
    """
    s1 = {'red', 'purple', 'pink', 'red', 'red', 'green', 'yellow', 'orange'}
    s2 = {'purple', 'pink', 'black', 'yellow', 'brown'}


    print(s1)
    print(s2)

    print(s1 & s2)
    print(s1 ^ s2)
    print(s1 | s2)
    print(s1 - s2)
    print(s2 - s1)

def finding_unique_values():
    """
    How to find unique values in a sequence.

    :return:
    """
    food = ['spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs']

    f = set(food)
    print(f)

    f.add('toast')
    f.add('pancakes')
    f.add('toast')
    f.add('toast')
    f.add('toast')

    print(f)

if __name__ == '__main__':
    main()














