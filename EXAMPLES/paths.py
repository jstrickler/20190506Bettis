#!/usr/bin/python3

import sys
import os.path

unix_p1 = "/usr/local/bin/foo"
unix_p2 = "bin/foo.txt"

win_p1 = r"\\marmoset\sharing\technology\docs\bonsai\foo.doc"
win_p2 = r"bonsai\foo.doc"

if sys.platform == 'win32':
    print("dirname(win_p1): ",os.path.dirname(win_p1))
    print("dirname(win_p2): ",os.path.dirname(win_p2))
    print("basename(win_p1): ",os.path.basename(win_p1))
    print("basename(win_p2): ",os.path.basename(win_p2))
    print("os.path.split(win_p1) HEAD: {0[0]} TAIL: {0[1]}".format(os.path.split(win_p1)))
    print("os.path.split(win_p1) HEAD: {0[0]} TAIL: {0[1]}".format(os.path.split(win_p2)))
    print("os.path.splitunc(win_p1) HEAD: {0[0]} TAIL: {0[1]}".format(os.path.splitunc(win_p1)))
    print("os.path.splitunc(win_p1) HEAD: {0[0]} TAIL: {0[1]}".format(os.path.splitunc(win_p2)))
else:
    print("dirname(unix_p1): ",os.path.dirname(unix_p1))
    print("dirname(unix_p2): ",os.path.dirname(unix_p2))
    print("basename(unix_p1): ",os.path.basename(unix_p1))
    print("basename(unix_p2): ",os.path.basename(unix_p2))
    print('expanduser("~"): ',os.path.expanduser("~"))
    print('expanduser("~jstrick"): ',os.path.expanduser("~jstrick"))
    print("isabs(unix_p1): ",os.path.isabs(unix_p1))
    print("isabs(unix_p2): ",os.path.isabs(unix_p2))
    print("os.path.split(unix_p1) HEAD: {0[0]} TAIL: {0[1]}".format(os.path.split(unix_p1)))
    print("os.path.split(unix_p2) HEAD: {0[0]} TAIL: {0[1]}".format(os.path.split(unix_p2)))
