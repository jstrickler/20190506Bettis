#!/usr/bin/env python
from PIL import Image

im = Image.open('../DATA/felix_auto.jpeg')
print(im.format)
print(im.size)
print(im.mode)

im.save('felix_auto.png')



