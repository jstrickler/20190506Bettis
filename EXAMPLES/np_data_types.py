#!/usr/bin/env python
import numpy as np

r1 = np.arange(45)
r1.shape = (3,3,5)
print('r1 =>\n', r1)

r2 = np.arange(45, dtype=np.float)
r2.shape = (3,3,5)
print('r2 =>\n', r2)

