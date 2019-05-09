#!/usr/bin/env python

'''
    sp_misc

    created 2014 by jstrick
'''
import scipy as sp

import sys
print(sys.modules['scipy'])

from scipy.fftpack import cs_diff


x = sp.array([1,2,3])
print(x)
print(type(x))


def main():
    print(sp.info(cs_diff))
    print('-' * 60)
    print(sp.source(cs_diff))



if __name__ == '__main__':
    main()
