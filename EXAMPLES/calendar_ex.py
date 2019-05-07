#!/usr/bin/python3

import sys
import calendar

tcal = calendar.TextCalendar()
print(tcal.formatmonth(2012,1))

print()

hcal = calendar.HTMLCalendar()
print(hcal.formatmonth(2012,1))

