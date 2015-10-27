import urllib.request

def docstringtest():
    """
    test docstring
    :return:
    """
    print('hallo')







url = urllib.request.urlopen('http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=b7w5qxk8dqtvbntnx5uns434fhww6878&dag=27-10-2015&sorteer=0')
bestand = open('lucasklad', 'a')
bestand.write(str(url))
bestand.close()