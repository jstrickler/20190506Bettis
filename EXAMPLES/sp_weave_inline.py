#!/usr/bin/env python

import scipy
print(dir(scipy))
print(scipy.version.short_version)
from scipy import weave
import numpy as np
  
def times_n(seq, n):

    code = r'''
    #include <stdio.h>
    int val;
    for (int i = 0; i < seq.length(); i++) {
        val = py_to_int(PyList_GetItem(seq,i),"val");
        printf("%02d %d\n", i, val * n);
    }
    '''

    return weave.inline(code,['seq','n'])

times_n([1,5,9], 10)
times_n([2,4,6,8,10,12], 30)


def blitz_test(values):
    c_code = r'''
#include <stdio.h>
int tmp;
for (int i = 0; i < values.length(); i++) {
    tmp = PyList_GetItem(values, i);
    Py
}

    '''

x = np.arange(10)
