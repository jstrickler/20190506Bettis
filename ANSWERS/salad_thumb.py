#!/usr/bin/env python
"""

@author: jstrick
Created on Sat Jun 15 03:51:37 2013

"""
import Image

im = Image.open('../DATA/salad.jpeg')

size = 50, 50
im.thumbnail(size)
im.save('salad_thumb.jpg')

