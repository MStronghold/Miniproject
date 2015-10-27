import urllib.request
import time





def docstringtest():
    """
    test docstring
    :return:
    """
    print('hallo')



def API(x):
    url = 'http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=b7w5qxk8dqtvbntnx5uns434fhww6878'
    tijd = time.strftime('%d/%m/%y')
    url += '&dag=' + str(tijd)
    url += '&sorteer=' + x


url = urllib.request.urlopen('http://www.filmtotaal.nl/api/filmsoptv.xml?apikey=b7w5qxk8dqtvbntnx5uns434fhww6878&dag=27-10-2015&sorteer=0')
bestand = open('lucasklad', 'a')
bestand.write(str(url))
bestand.close()
