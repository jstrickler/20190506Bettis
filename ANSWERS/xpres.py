#!/usr/bin/python

from xml.etree import ElementTree as ET

pres_doc = ET.parse('../DATA/presidents.xml')

for pres in pres_doc.findall("president"):
    full_name = pres.findtext('name/last') + ' ' + pres.findtext('name/first')
    state = pres.findtext('birthstate')
    print(('{0:40s} {1:30s}'.format(full_name,state)))