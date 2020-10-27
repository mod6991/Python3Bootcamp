import xml.etree.ElementTree as ET
from xml.dom import minidom

# -------------
# Read XML file
# -------------

tree = ET.parse('countries.xml')
root = tree.getroot()
#root = ET.fromstring(country_data_as_string)

for child in root:
    print(f"{child.tag} -> {child.attrib}")

panama = root.find("./country[@name='Panama']")
panama_gdppc = panama.find('./gdppc')
print(panama_gdppc.text)

liechtenstein_neighbors = root.findall("./country[@name='Liechtenstein']/neighbor")
for neighbor in liechtenstein_neighbors:
    print(f"{neighbor.attrib['name']} direction: {neighbor.attrib['direction']}")

# --------------
# Write XML file
# --------------

# create the file structure
data = ET.Element('data')
items = ET.SubElement(data, 'items')
item1 = ET.SubElement(items, 'item')
item2 = ET.SubElement(items, 'item')
item1.set('name','item1')
item2.set('name','item2')
item1.text = 'item1abc'
item2.text = 'item2abc'

# create a new XML file with the results
mydata = ET.tostring(data, encoding='utf-8')
reparsed = minidom.parseString(mydata)
final_data = reparsed.toprettyxml(indent="  ")
myfile = open("items.xml", "w", encoding='utf-8')
myfile.write(final_data)