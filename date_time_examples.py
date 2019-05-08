#!/usr/bin/env python
from datetime import date, time, datetime, timedelta
import time as Time
import calendar

# from Anaconda
from dateutil.parser import parse

#  6-20-2018   Ambrose

today = date.today()
ambrose_bd = date(2018, 6, 20)

print(today, ambrose_bd)
print(today.strftime('%B %d, %Y'))
print(ambrose_bd.strftime('%b %b %y'))

days_alive = today - ambrose_bd

print(days_alive)
print(days_alive.days)

years, days = divmod(days_alive.days, 365)

print(f"Ambrose is {years} years and {days/30:.0f} months old")


dates = [
    "June 20, 2018",
    "20 June 2018",
    "6-20-2018",
    "Jun 20th, 2018",
    "June 20th 18",
    "Jurgle 20th 2018",
    "June 49th, 1234",
    "September 8, 1752",
]


for d in dates:
    try:
        print(f"{d:20} {parse(d).date()}")
    except Exception as err:
        print(err)

print("Wait for it....", flush=True, end='')
Time.sleep(1.5)
print("done.")

print(Time.time())




