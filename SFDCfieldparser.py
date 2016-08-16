#using elementtree api this parser will output all fields, their type and text values set in header_row in a csvfile labeled {input}.csv from the 1 command line argument
#change the header_row for new fields>tags values, it will ignore any tags not in header_row (for fields)
#alter the root.iter('change this') attribute to parse non "fields" tags (you'll need to alter header_row probably too for non fields child tags)
#DO NOT PARSE UNKNOWN XML WITH THIS FUNCTION AS THERE ARE VULNERABILITIES THAT IT DOES NOT PROTECT AGAINST
import xml.etree.ElementTree as ET
import csv
import os
import sys

sourcefile = sys.argv[1]
tree = ET.parse(open(sourcefile, "r"))
root = tree.getroot()
#print root.items()


def get_fields_list_CSV(root):
    with open(sourcefile+'.csv', 'w') as csvfile:
        header_row=['fullName','label','externalId','type', 'formula','formulaTreatBlanksAs', 'unique', 'required', 'referenceTo', 'relationshipName','relationshipLabel']
        writer = csv.DictWriter(csvfile, fieldnames=header_row,delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL, extrasaction='ignore')
        writer.writeheader()
        for e in root.iter('{http://soap.sforce.com/2006/04/metadata}fields'):
            field_row = {}
            for m in e:
                val = {m.tag[41:]:m.text}
                field_row.update(val)
                #print val
            #print field_row
            writer.writerow(field_row)
            #print e



get_fields_list_CSV(root)
print sourcefile +" "+'Was Parsed!'
