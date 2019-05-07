#!/usr/bin/python 
import sys
try:
    import lxml.etree as ET
except ImportError:
    import xml.etree.ElementTree as ET

with open('../DATA/words.txt') as WORDS:
    xwords = [ word[:-1] for word in WORDS if word.startswith('x') ]

root = ET.Element('words')
for word in xwords:
    word_element = ET.Element('word')
    word_element.text = word 
    root.append(word_element)

tree = ET.ElementTree(root)

if sys.modules['lxml']:
    tree.write('xwords.xml', pretty_print=True)
else:
    tree.write('xwords.xml')
