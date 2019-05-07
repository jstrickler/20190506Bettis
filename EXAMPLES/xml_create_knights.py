#!/usr/bin/env python

'''Create a print a new XML document'''
from collections import namedtuple

HAS_LXML = False

try:
    import lxml.etree as ET
    HAS_LXML = True
except ImportError:
    import xml.etree.ElementTree as ET

FILE_NAME = 'knights.xml'
FIELDS = ['title', 'color', 'quest', 'comment']

def main():
    '''Program entry point'''
    knight_info = get_knight_info()
    knight_root = build_tree(knight_info)
    knight_doc = ET.ElementTree(knight_root)
    write_doc(knight_doc)

def get_knight_info():
    '''Read knight data from the file'''
    info = []
    with open('../DATA/knights.txt') as kn:
        for line in kn:
            flds = line[:-1].split(':')
            info.append(flds)
    return info

def build_tree(knight_recs):
    '''Build the new XML document'''
    tree = ET.Element('knights')
    for knight_rec in knight_recs:
        knight_element = ET.Element('knight', name=knight_rec[0])
        for tag_name, tag_value in zip(FIELDS, knight_rec[1:]):
            sub_element = ET.Element(tag_name)
            sub_element.text = tag_value
            knight_element.append(sub_element)
        tree.append(knight_element)
    return tree

def write_doc(doc):
    '''Write the XML document out to a file, pretty-printing if available'''
    if HAS_LXML:
        doc.write(FILE_NAME, pretty_print=True)
    else:
        doc.write(FILE_NAME)

main()