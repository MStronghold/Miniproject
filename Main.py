
# Library's
import time
import urllib.request

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
        tijd = time.strftime('%d/%m/%y')
        url += '&dag=' + str(tijd)
        url += '&sorteer=' + str(x)
        try:
            return urllib.request.urlopen(url)
        except:
            return 'Kan geen verbinding maken.'

print(API(2))