#!/usr/bin/env python
# (c) 2017 John Strickler
#
import h5py
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

DATA_FILE = '../DATA/h5/TSX_SM_053_0008_20111223-20121026_0308_00063.h5'

DATASET_NAME =   '/GEOCODE/unwrapped_interferogram'


hfile = h5py.File(DATA_FILE)

dset = hfile[DATASET_NAME]

print(dset[475:480, 195:205])

rows = range(475, 486, 5)

for row in rows:
    plt.plot(dset[row, 195:500], '-', linewidth=2)

plt.show()
