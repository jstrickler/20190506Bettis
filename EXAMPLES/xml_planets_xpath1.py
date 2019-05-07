#!/usr/bin/env python

'''Use XPath to extract planets from solar.xml'''

import xml.etree.ElementTree as ET
from itertools import chain

def main():
    '''Program entry point'''
    doc = ET.parse('../DATA/solar.xml')
    
    # can search from doc -- no need to get root element
    #  // means match any number of nested tag levels
    inner_planets = doc.find('.//innerplanets')
    outer_planets = doc.find('.//outerplanets')
    
    print('Inner:')
    for planet in inner_planets:
        print('\t', planet.get("name"))
    
    print('Outer:')
    for planet in outer_planets:  # + outer_nodes:
        print('\t', planet.get("name"))
    
    print("-" * 50)
    # use itertools.chain to treat multiple iterables as a single iterable
    for planet in chain(inner_planets, outer_planets):
        print(planet.get('name'))
        
main()