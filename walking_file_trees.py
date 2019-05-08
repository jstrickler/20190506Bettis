#!/usr/bin/env python
import os

#     (dir, subdirs, files)
#  for TUPLE in os.walk(START_DIR):
#      .....

START_DIR = os.path.abspath('.')

for curr_dir, subs, files in os.walk(START_DIR):
    if '.git' in curr_dir:
        continue
    print(curr_dir)
    for file_name in files:
        if file_name.endswith('.py'):
            file_path = os.path.join(curr_dir, file_name)
            file_size = os.path.getsize(file_path)
            print(f"    {file_size:6d} {file_name}")


