#!/usr/bin/python3

import sys

import time

right_now = time.time()
print("It is {0} seconds since 1/1/70".format(right_now))

time.sleep(5)

now_asc = time.asctime()
print("it is now",now_asc)
now_ctime = time.ctime()
print("it is now",now_ctime)

time_str = "Jan 14, 1971"
print('Time string:',time_str)

parsed_time = time.strptime(time_str, '%b %d, %Y')
print("Parsed time is",parsed_time)

print('Formatted time:',time.strftime("%m/%d/%y %I:%M",parsed_time))

