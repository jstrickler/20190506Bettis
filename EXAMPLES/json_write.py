#!/usr/bin/env python

import json

george = [
    {
        'num': 1,
        'lname': 'Washington',
        'fname': 'George',
        'dstart': [1789, 4, 30],
        'dend': [1797, 3, 4],
        'birthplace': 'Westmoreland County',
        'birthstate': 'Virginia',
        'dbirth': [1732,2,22],
        'ddeath': [1799,12,14],
        'assassinated': False,
        'party': None,
}
]

js = json.dumps(george,indent=4)
print(js)

with open('george.json','w') as JS:
    json.dump(george,JS, indent=4)