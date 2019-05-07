#!/usr/bin/env python
from PIL import Image

box = (1200, 100, 2000, 400)
im = Image.open('../DATA/felix_auto.jpeg')
region = im.crop(box)
region = region.transpose(Image.FLIP_LEFT_RIGHT)
im.paste(region,box)
im.save('felix_auto_cropped.jpg')
