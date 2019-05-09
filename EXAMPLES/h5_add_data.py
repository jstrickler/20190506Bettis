#!/usr/bin/env python
# (c) 2017 John Strickler
#
import h5py

H5_FILE = '../DATA/h5/hdf5_test.h5'

with h5py.File(H5_FILE) as hfile:
    ds1 = hfile.create_dataset('/Animals/giraffe', (15, 2))
    ds2 = hfile.create_dataset(
        '/Animals/coatimundi', (15, 2), dtype='i8'
    )
    ds2[0] = [5, 10]
    ds2.attrs['start_date'] = '2019-05-08'
    ds2.attrs['creator'] = 'John Strickler'



