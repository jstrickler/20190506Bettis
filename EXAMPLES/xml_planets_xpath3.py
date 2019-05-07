#!/usr/bin/env python

import xml.etree.ElementTree as ET
'''Parse planets from solar.xml using XPath'''

def main():
    '''Program entry point'''
    for planet in ET.parse('../DATA/solar.xml').findall('.//planet'):
        print(planet.get('name'))
        
main()