# SFDCfieldparser
quick python script to extract all fields from SFDC object metadata files

# Usage: 
## XML to CSV
### python SFDCfieldparser.py <path to SFDC metadata files>

## XML to JSON
- run this script from the command line like this:
  - usage: python xml_to_json.py file1.xml file2.xml file3.xml 
  - The script will create file1.xml.json, file2.xml.json, and file3.xml.json
  - The JSON files will be formatted with indentation and line breaks to make them easier to read
  - The JSON files will be saved in the same directory as the XML files
  - The script will overwrite any existing JSON files with the same name
  - The script will not delete any existing JSON files that are not specified in the command line arguments
  - The script will not delete the XML files

