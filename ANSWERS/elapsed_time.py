#!/usr/bin/python

import sys
import datetime

if len(sys.argv) < 2:
    print("Please enter a date in format YYYY-MM-DD")
    sys.exit(1)

(year,month,day) = sys.argv[1].split("-")

that_date = datetime.date(int(year),int(month),int(day))

elapsed = datetime.date.today() - that_date

print("%d years %d days" % (elapsed.days / 365.25, elapsed.days % 365))
