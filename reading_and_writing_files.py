#!/usr/bin/env python

with open('DATA/mary.txt') as mary_in:
    print(type(mary_in))
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print()

with open('DATA/mary.txt') as mary_in:
    all_lines = mary_in.readlines()
    print(all_lines)
print()

with open('DATA/mary.txt') as mary_in:
    whole_file = mary_in.read()
    print(whole_file, '\n')
    print(repr(whole_file))

# x = mary_in.readlines()


# mary_in = open(...)
#  ...
# mary_in.close()

#  A in B      is A contained in B

#  for VAR ...   in ITERABLE:
#      ...

x = 5
xt = type(x)
print(xt)

M_THING = xt(42)
print(M_THING)

FRUITS = ["pomegranate", "cherry", "apricot", "Apple",
          "lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
          "Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
          "elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date"]

with open('fruitdata.txt', 'w') as fruitdata_out:
    for fruit in FRUITS:
        fruitdata_out.write(fruit.upper() + '\n')

with open('fruitdata2.txt', 'w') as fruitdata_out:
    fruitdata_out.writelines(f.upper() + '\n' for f in FRUITS)
