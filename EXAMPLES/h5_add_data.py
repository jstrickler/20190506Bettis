#!/usr/bin/env python
# (c) 2017 John Strickler
#
import h5py

H5_FILE = '../DATA/h5/hdf5_test.h5'

with h5py.File(H5_FILE) as hfile:
    ds1 = hfile.create_dataset('/Animals/wombat', (15, 2))
    ds2 = hfile.create_dataset(
        '/Animals/bushbaby', (15, 2), dtype='i8'
    )

