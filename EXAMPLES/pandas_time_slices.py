#!/usr/bin/env python
"""

@author: jstrick
Created on Sun Jun  2 09:48:50 2013

"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# every hour for 3 days
hourly = pd.date_range('1/1/2013 00:00:00','1/3/2013 23:59:59', freq='H')
print("Number of periods: ",len(hourly))

# every second for 18 hours
seconds = pd.date_range('1/1/2013 12:00:00',freq='S',periods=(60*60*18))
print("Number of periods: ", len(seconds))
print("Last second: ",seconds[-1])

# every month for 1 year
monthly = pd.date_range('1/1/2013','12/31/2013', freq='M')
print("Number of periods: {0} Seventh element: {1}".format(
    len(monthly), 
    monthly[6]
))

NUM_DATA_POINTS = 1441   # number of minutes in a day

# create range from starting point with specified number of points
# one day's worth of minutes
dates = pd.date_range('4/1/2013 00:00:00', periods=NUM_DATA_POINTS, freq='T')

# a day's worth of data
data = np.random.random(NUM_DATA_POINTS)

# series indexed by minutes
series = pd.Series(data,index=dates)

# grab the half hour of data from 10:00 to 10:30
time_slice = series['4/1/2013 10:00:00':'4/1/2013 10:30:00']
print(time_slice)   # 31 values

