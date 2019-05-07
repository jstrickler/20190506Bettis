#!/usr/bin/env python

code = """
class = "Senior"
"""

try:
    eval(code)
except SyntaxError as err:
    print(err)

