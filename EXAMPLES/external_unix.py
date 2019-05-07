#!/usr/bin/python3

import sys
import os

if sys.platform == 'win32':
    print("This script only runs on non-Windows systems")
    sys.exit(1)

os.system("who")

ls = os.popen("ls -l /tmp","r")

for entry in ls:
    print(entry[:-1])
print()

# backticks equivalent
h = os.popen("uname -n").read()[:-1]

print(h)
