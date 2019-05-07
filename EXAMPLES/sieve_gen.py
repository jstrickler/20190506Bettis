#!/usr/bin/python

def primes(limit):
    flags = [False] * (limit+1)  # initialize flags

    for i in range(2,limit):
        if flags[i]:
            continue
        for j in range(2*i,limit+1,i):
            flags[j] = True
        yield i  # execution stops here until next value is requested by for-in loop

prime_gen = primes(100)
for p in prime_gen:
    print(p, end=' ')

