#!/usr/bin/python

import sys
import datetime

if len(sys.argv) < 3:
    print("Please enter two dates in format YYYY-MM-DD")
    sys.exit(1)

(year,month,day) = sys.argv[1].split("-")
this_date = datetime.date(int(year),int(month),int(day))

(year,month,day) = sys.argv[2].split("-")
that_date = datetime.date(int(year),int(month),int(day))

elapsed =  that_date - this_date

print("%d years %d days" % (elapsed.days / 365.25, elapsed.days % 365.25))
