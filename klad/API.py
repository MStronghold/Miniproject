"""
Lucas: Bevat alle functies voor interactie met OMDB API.

Functies:

"""
from urllib.request import urlopen
from ast import literal_eval

def urlhandler(x):
    """
    Invoerfunctie voor zoekveld.
    Accepteert string(titel of idnummer)
    en returned API url naar APIrequest():.
    :param x:
    :return:
    """

    url = 'http://www.omdbapi.com/?'
    if x[:2] == 'tt':
        url += 'i=' + x
    else:
        url += 't=' + x
    APIrequest(url)


def APIrequest(url):
    try:
        with urlopen(url) as f:
            data = f.read().decode()
        print(data, '\n', '--', '\n')
        outputhandler(data)
    except:
        print(url)
        print('verbindingsfout', '\n')
        urlhandler()


def outputhandler(x):
    gegevens = literal_eval(x)
    for key in gegevens:
        print(key, gegevens[key], '\n')







