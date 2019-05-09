#!/usr/bin/env python


def spam(foo, bar, /):
    print(foo, bar)


spam(1, 2)
spam(bar=5, foo=20)
