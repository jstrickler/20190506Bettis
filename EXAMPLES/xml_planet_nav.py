#!/usr/bin/env python

'''Use etree navigation to extract planets from solar.xml'''

try:
    import lxml.etree as ET
except ImportError:
    import xml.etree.ElementTree as ET

def main():
    '''Program entry point'''
    doc = ET.parse('../DATA/solar.xml')
    
    solar_system = doc.getroot()  # get the solarsystem tag
    
    print(solar_system)
    print()
    
    inner = solar_system.find('innerplanets')
    print('Inner:')
    
    for planet in inner:  # loop through children
        if planet.tag == 'planet':
            print('\t', planet.get("name", "NO NAME"))
            
    outer = solar_system.find('outerplanets')
    print('Outer:')
    
    for planet in outer:  # loop through children
        print('\t', planet.get("name"))
            
    plutoids = solar_system.find('plutoidplanets')
    print('Plutoid:')
    
    for planet in plutoids:  # loop through children
        print('\t', planet.get("name"))

if __name__ == '__main__':
    main()