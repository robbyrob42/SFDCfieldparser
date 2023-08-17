# usage: python xml_to_json.py file1.xml file2.xml file3.xml
# The script will create file1.xml.json, file2.xml.json, and file3.xml.json
# The JSON files will be formatted with indentation and line breaks to make them easier to read
# The JSON files will be saved in the same directory as the XML files
# The script will overwrite any existing JSON files with the same name
# The script will not delete any existing JSON files that are not specified in the command line arguments
# The script will not delete the XML files

import xml.etree.ElementTree as et
import json
import sys


def xml_to_json(sourcefile):
    # Construct the output filename
    filename_out = sourcefile + '.json'

    # Parse the XML document
    tree = et.parse(open(sourcefile, "r"))
    root = tree.getroot()
    if root is not None:
        print(root.text)
    dict_list = []

    # Iterate over the <fields> elements
    for fields in root.findall('{http://soap.sforce.com/2006/04/metadata}fields'):
        # create a dictionary for this <fields> element
        fields_dict = {}

        # iterate over the child elements of <fields>
        for child in fields:
            # store the text of the element in the dictionary
            # using the tag (without namespace) as the key
            fields_dict[child.tag.split('}')[-1]] = child.text

        # append the dictionary to the list
        dict_list.append(fields_dict)

    # # Iterate over the <fields> elements
    # for fields in root.findall('{http://soap.sforce.com/2006/04/metadata}fields'):
    #     # Find the <fullname>, <label>, and <type> elements and get their text
    #     if fields.find('{http://soap.sforce.com/2006/04/metadata}fullName') is not None:
    #         fullname = fields.find('{http://soap.sforce.com/2006/04/metadata}fullName').text
    #     else:
    #         fullname = 'None'
    #     if fields.find('{http://soap.sforce.com/2006/04/metadata}label') is not None:
    #         label = fields.find('{http://soap.sforce.com/2006/04/metadata}label').text
    #     else:
    #         label = 'None'
    #     if fields.find('{http://soap.sforce.com/2006/04/metadata}type') is not None:
    #         type_ = fields.find('{http://soap.sforce.com/2006/04/metadata}type').text
    #     else:
    #         type_ = 'None'
    #
    #     # Store the text in a dictionary
    #     dict_ = {'fullname': fullname, 'label': label, 'type': type_}
    #     print(dict_)
    #
    #     # Append the dictionary to the list
    #     dict_list.append(dict_)

    # Write the list of dictionaries to a JSON file
    with open(filename_out, 'w') as file:
        file.write(json.dumps(dict_list, indent=4))


# Get the list of XML filenames from the command line arguments
xml_files = sys.argv[1:]

# Convert each XML file to JSON
for xml_file in xml_files:
    xml_to_json(xml_file)
