#!/usr/bin/env python

'''Use XPath to find Jupiter's moons from solar.xml'''

import xml.etree.ElementTree as ET

def main():
    '''Program entry point'''
    doc = ET.parse('../DATA/solar.xml')
    
    jupiter = doc.find('.//planet[@name="Jupiter"]')
    
    for moon in jupiter:
        print(moon.text)
        
main()