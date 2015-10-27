import xml.etree.ElementTree as etree

xmlD = etree.parse("test.xml")
root = xmlD.getroot()

for child in root:
    for childeren in child:
        print(childeren.text)
    print("\n")