#!/usr/bin/python

import datetime

def make_date(date_string):
    raw_year, raw_month, raw_day = date_string.split('-')
    year = int(raw_year)
    month = int(raw_month)
    day = int(raw_day)

    return datetime.date(year, month, day)


pres_lname = input("Enter president's last name: ")

with open("../DATA/presidents.txt") as PRES:
    for rec in PRES:
        flds = rec.split(":")
        if flds[1].lower().startswith(pres_lname.lower()):
            birth_date = make_date(flds[3])

            if flds[4] != "NONE":
                alive = False
                death_date = make_date(flds[4])
            else:
                alive = True
                death_date = datetime.date.today()

            print("NAME: {0} {1}".format( flds[2],flds[1] ))
            print("BIRTH:", birth_date)
            print("DEATH:", end='')
            if alive:
                print('* * *')
            else:
                print(death_date)
            
            # calculate age
            lifespan = death_date - birth_date
            age = lifespan.days/365.25

            print('AGE: {0:.2f}'.format(age))
