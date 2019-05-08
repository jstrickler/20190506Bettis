#!/usr/bin/env python
import numpy as np

a = np.loadtxt(
    '../DATA/columns_of_numbers.text',
    usecols=[2, 3],
    skiprows=1,
)

print(a)
print(a.shape)
print(a.size)
