#!/usr/bin/env python
"""

@author: jstrick
Created on Sat Jun 15 03:51:37 2013

"""
import Image

im = Image.open('../DATA/salad.jpeg')

im_flipped = im.transpose(Image.FLIP_LEFT_RIGHT)
im_flipped.save('salad_flipped.jpeg')
