#!/usr/bin/env python
import os

print(os.getenv('CONDA_PREFIX'))

print(os.getenv('WOMBAT_PREFIX'))
print(os.getenv('WOMBAT_PREFIX', 'brown-nosed'))

