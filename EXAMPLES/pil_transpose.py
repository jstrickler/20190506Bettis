#!/usr/bin/env python

from PIL import Image
SMALLSIZE = 200,200
im = Image.open('../DATA/felix_auto.jpeg')
im_small = im.resize(SMALLSIZE)

im1 = im_small.rotate(45)
im1.save('felix_auto_45.jpg')

im2 = im_small.transpose(Image.FLIP_LEFT_RIGHT)
im2.save('felix_auto_flipLR.jpg')

im3 = im_small.transpose(Image.FLIP_TOP_BOTTOM)
im3.save('felix_auto_flipTB.jpg')
