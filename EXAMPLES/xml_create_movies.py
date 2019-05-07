#!/usr/bin/env python

'''Create a print a new XML document'''

HAS_LXML = False

try:
    import lxml.etree as ET
    HAS_LXML = True
except ImportError:
    import xml.etree.ElementTree as ET
            
def main():
    '''Program entry point'''
    root = build_tree()
    doc = ET.ElementTree(root)
    print_doc(root)
    write_doc(doc)

def build_tree():
    '''Build the new XML document'''
    root = ET.Element('movies')
    
    for movie in ('Superman Returns', 'This is Spinal Tap'):
        movie_element = ET.Element('movie')
        movie_element.text = movie
        root.append(movie_element)
    
    movie = ET.Element('movie', director='Spielberg, Stephen')
    root.append(movie)
    movie.text = 'Jaws'
    
    movie = ET.Element('movie', director='Hitchcock, Alfred')
    movie.text = 'Vertigo'
    actor1 = ET.Element('actor')
    actor1.text = 'James Stewart'
    movie.append(actor1)
    actor2 = ET.Element('actor')
    actor2.text = 'Kim Novak'
    movie.append(actor2)
    root.append(movie)
    
    movie3 = ET.Element('movie', director='Welles, Orson')
    movie3.text = 'Citizen Kane'
    root.append(movie3)

    return root

def print_doc(root):
    '''Print out the XML document, pretty-printing if available'''
    if HAS_LXML:
        print(ET.tostring(root, pretty_print=True).decode())
    else:
        print(ET.tostring(root).decode())

def write_doc(doc):
    '''Write the XML document out to a file, pretty-printing if available'''
    if HAS_LXML:
        doc.write('movies.xml', pretty_print=True)
    else:
        doc.write('movies.xml')

main()
