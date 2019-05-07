#!/usr/bin/env python
"""

@author: jstrick
Created on Sat Jun 15 03:51:37 2013

"""
import Image

im = Image.open('../DATA/salad.jpeg')

height = im.size[0]
width = im.size[1]

new_height = height/2
new_width = width/2

new_size = new_height, new_width

im_half = im.resize(new_size)

im_half.save('salad_half.jpeg')
