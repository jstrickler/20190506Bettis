#!/usr/bin/env python

while True:
    file_name = input("Enter file name: ")
    file_name = file_name.strip()

    if file_name.lower() == 'q':
        break

    if file_name == '':
        continue

    print(f"Processing {file_name}")
