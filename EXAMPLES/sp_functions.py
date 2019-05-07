#!/usr/bin/env python
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

dt = np.dtype([('Month', 'int8'), ('Day', 'int8'), ('Year', 'int16'), ('Temp', 'float64')])
data = np.loadtxt('../DATA/weather/NYNEWYOR.txt',dtype=dt)

print(data['Temp'])

days = range(len(data['Temp']))
temps = data['Temp']

plt.plot(days, temps )
plt.savefig('first_plot.pdf')
plt.cla()  # clear first axis but not the whole figure

# hmmm -- some anomalous data
# let's remove readings < -50, which seem to be default N/A values
normalized_data = data[ data['Temp'] > -50 ]
days = range(len(normalized_data))
temps = normalized_data['Temp']
plt.plot(days, temps)
plt.savefig('second_plot.pdf')
