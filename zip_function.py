#!/usr/bin/env python
from pprint import pprint

first_words = ["Big", 'So', 'Not', 'Never']
middle = ['Honking', 'Bleeding', 'Much']
second_words = ["Deal", 'What', 'Impressed']

phrases = zip(first_words, middle, second_words)
print(phrases)

for phrase in phrases:
    print(phrase)



field_names = """term lastname firstname birthdate deathdate
birthplace birthstate termstart termend party""".split()

presidents = []

with open('DATA/presidents.txt') as pres_in:
    for raw_line in pres_in:
        fields = raw_line.rstrip().split(':')
        kv_pairs = zip(field_names, fields)
        pres_dict = dict(kv_pairs)
        presidents.append(pres_dict)


pprint(presidents)

print(presidents[0]['birthdate'])
print(presidents[25]['lastname'])
print(presidents[25])



