#!/usr/bin/env python

values = 10, 'cheese', 1.3, None, 0

for value in values:
    try:
        result = 5 + value
        print("Added 5 to", value)
    except TypeError as err:
        print("ERROR:", err)
    else:
        print("Result is", result)   # prints if no errors
    finally:
        print('-' * 50)   # always prints
