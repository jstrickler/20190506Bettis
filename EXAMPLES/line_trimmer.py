#!/usr/bin/python

def line_trimmer(file_name):
    with open(file_name) as file_in:
        for line in file_in:
            yield line.rstrip('\n\r')

mary_in = line_trimmer('../DATA/mary.txt')
for line in mary_in:
    print(line)

