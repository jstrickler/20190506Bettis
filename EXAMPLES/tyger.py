#!/usr/bin/env python

with open("../DATA/tyger.txt") as f:
    for line in f:
        print(line[:-1])
