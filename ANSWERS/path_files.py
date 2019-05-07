#!/usr/bin/python

import os

path = os.getenv('PATH')
paths = path.split(os.pathsep)

for path_dir in paths:
    all_files = os.listdir(path_dir)
    print("{0}: {1}".format(path_dir,len(all_files)))
