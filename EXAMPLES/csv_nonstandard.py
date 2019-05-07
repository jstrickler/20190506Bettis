#!/usr/bin/env python
"""

@author: jstrick
Created on Sun Mar 10 16:36:31 2013

"""
import csv

with open('../DATA/computer_people.txt') as computer_people_in:
    rdr = csv.reader(computer_people_in, delimiter=';')

    for first_name, last_name, known_for in rdr:
        print('{}: {}'.format(last_name, known_for))

