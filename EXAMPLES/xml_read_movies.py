#!/usr/bin/env python

import xml.etree.ElementTree as ET

movies_doc = ET.parse('movies.xml')

movies_root = movies_doc.getroot()

for movie_node in movies_root:
    print(movie_node.text)
    for actor in movie_node:
        print('\t',actor.text)
