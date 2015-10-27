#Methode 1
import xmltodict

def verwerk_xml():
    bestand = open('test.xml', 'r')
    xml_string = bestand.read()
    return xmltodict.parse(xml_string)

stations_dict = verwerk_xml()
print(stations_dict['catalog'],['book'],['author'])


#Methode 2
import xml.etree.ElementTree as etree

xmlD = etree.parse("test.xml")
root = xmlD.getroot()

for child in root:
    for childeren in child:
        print(childeren.text)
    print("\n")