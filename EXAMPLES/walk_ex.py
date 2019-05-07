#!/usr/bin/python3
import os
'''print size of every python file whose name starts with "m" '''

START_DIR = ".."   # start in root of student files

def main():
    for currdir,subdirs,files in os.walk(START_DIR):
        for file in files:
            if file.endswith('.py') and file.startswith('m'):
                fullpath = os.path.join(currdir,file)
                fsize = os.path.getsize(fullpath)
                print("{0:8d} {1:s}".format(fsize, fullpath))

if __name__ == '__main__':
    main()
