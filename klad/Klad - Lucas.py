
# Library's
import time
import urllib.request
import xml.etree.ElementTree as ET

def API(x):
    """
    0=alle films
    1=filmtips
    2=film vd dag
    :return:
    """
    if type(x) is not int:
        raise TypeError('API(x) x is not int')
    elif x < 0 or x > 2:
        raise AttributeError('API(x) Parameter out of bounds')
    else:
        url = 'http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=b7w5qxk8dqtvbntnx5uns434fhww6878'
        tijd = time.strftime('%d-%m-%Y')
        url += '&dag=' + str(tijd)
        url += '&sorteer=' + str(x)
        try:
            print(url)
            return urllib.request.urlopen(url)
        except:
            return 'Kan geen verbinding maken.'

with open('lucasklad-bronlatin.txt', 'r') as infile:
    with open('lucassklad-doelutf.txt', 'w+') as outfile:
        bron = infile.read()
        doel = bytes(bron, 'iso-8859-1').decode('utf-8')
        outfile.write(doel)



# data = ET.parse(API(0))
# with open('test.xml', 'w+') as bestand:
#     for child in data.iter():
#         datastring = ET.tostring(child).decode('iso-8859-1')
#         datastring.encode('utf-8')
#         bestand.write(str(datastring) + '\n')


# datastring = ET.tostring(child).decode()
