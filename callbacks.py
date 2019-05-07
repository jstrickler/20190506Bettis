#!/usr/bin/env python


def doit(some_function, *args, **kwargs):
    print("running function:")
    some_function(*args, **kwargs)
    return 42

def spam(whom):
    print("Hello from", whom)
    return "wombat"

def ham():
    print("To BE, or NOT TO be")

doit(spam, 'Mom')  # spam is a "callback", short for "callback function"
doit(ham)

def toast():
    return ham

doit(toast())


