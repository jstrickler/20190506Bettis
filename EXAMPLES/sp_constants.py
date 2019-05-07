#!/usr/bin/env python

from scipy import constants as K

print("pi: {0}".format(K.pi))
print("Planck: {0}".format(K.Planck))
print("c (speed of light): {0}".format(K.c))

print("natural unit of energy: {0}".format(K.value('natural unit of energy')))
print("natural unit of energy (Unit): {0}".format(K.unit('natural unit of energy')))