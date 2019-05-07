#!/usr/bin/env python

def get_message():
    return "Hello, Bettis world"


def print_message():
    m = get_message()
    print(m)


def c2f(celsius):
    fahrenheit = ((9 * celsius) / 5) + 32
    return fahrenheit


f = c2f(100)
print(f)


def spam(req_pos, *opt_pos, req_named="Walter", **opt_named):
    print(req_pos)
    print(opt_pos)
    print(req_named)
    print(opt_named)

spam(5, req_named="spam")
spam(5, 6, 7, 8, req_named="spam", animal="wombat", color="red")

def print(p, *, end, sep):
    pass

print(sep=':', end='')

# pandas.read_csv('mydata.csv', index_col="hours")
