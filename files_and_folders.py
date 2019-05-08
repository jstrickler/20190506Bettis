#!/usr/bin/env python
import os
from datetime import datetime
from humanize import filesize

FOLDER = 'DATA'

FILE_NAME = 'alice.txt'

file_path = os.path.join(FOLDER, FILE_NAME)

print("file path:", file_path)

file_size = os.path.getsize(file_path)
print("file size:", filesize.naturalsize(file_size))

print(filesize.naturalsize(13029093033))

raw_timestamp = os.path.getmtime(file_path)
print("raw timestamp:", raw_timestamp)

timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp:", timestamp)

print(os.path.dirname(file_path))
print(os.path.basename(file_path))
print(os.path.abspath(file_path))

for x in 'alice.txt', 'wombat.txt', 'mary.txt', 'koalas.txt':
    print(x, os.path.exists(os.path.join('DATA', x)))
print()

if os.path.exists('DATA/betsy.txt'):
    os.rename('DATA/betsy.txt', 'DATA/mary.txt')

os.chmod('DATA/mary.txt', 0o777)
os.system("ls -l DATA/mary.txt")

os.chmod('DATA/mary.txt', 0o700)
os.system("ls -l DATA/mary.txt")

os.chmod('DATA/mary.txt', 0o000)
os.system("ls -l DATA/mary.txt")

os.chmod('DATA/mary.txt', 0o644)
os.system("ls -l DATA/mary.txt")


print(os.getcwd())
print(os.getuid())
print(os.getpid(), os.getppid())

print(os.listdir('DATA'))
print()

for entry in os.scandir('DATA'):
    if entry.name.endswith('.txt'):
        print(entry, entry.name, entry.is_dir(), entry.is_file())
        print(entry.stat(), '\n')
