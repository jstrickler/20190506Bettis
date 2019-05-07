#!/usr/bin/env python

try:
    with open('DATA/wombats.txt') as wombats_in:
        for raw_line in wombats_in:
            print(raw_line.rstrip())

except FileNotFoundError as err:
    print(err)

values = 5.1, 3.9, 0.0, 4.7, 'abc', 2.8

for v in values:
    try:
        result = 23.2 / float(v)
    except ZeroDivisionError as err:
        print(err)
        exit()
    except (ValueError, TypeError) as err:
        print(err)
    except Exception as err:
        print("Whoa! did not expect:", err)
    else:
        print(result)
    finally:
        print("v is", v)




