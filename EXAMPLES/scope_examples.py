#!/usr/bin/env python

x = 42
def function_a():
    y = 5

    def function_b():
        z = 32
        print("function_b(): z is", z)       # local scope
        print("function_b(): y is", y)       # nested (nonlocal) scope
        print("function_b(): x is", x)      # global scope
        print("function_b(): type(x) is", type(x))    # builtin scope
    return function_b;

f = function_a()   # calling function_a, which returns function_b
f()   # calling function_b
