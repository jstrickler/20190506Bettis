#!/usr/bin/env python

from PIL import Image

size = 125,125
im = Image.open('../DATA/felix_auto.jpeg')
im.thumbnail(size)
im.save('felix_auto_small.jpg')

