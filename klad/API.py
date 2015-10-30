"""
Volledige API afhandeling.

timeclocked at:
wall time: 4.9084945067253066e-06
ping is: 0.03187353219280745
Process time: 0.03253484027089535

API source:
http://www.omdbapi.com/

-Lucas, 29-10-15

"""
from urllib.request import urlopen      #http connector
from urllib import error                #error handling
from ast import literal_eval            #dict naar string converter
import re                               #regular expressions voor urlopbouw-filtering


def APIrequest(x):
    """
    Invoerfunctie voor zoekveld.
    Accepteert string(titel of idnummer),
    vraagt info en returned een dict met informatie.
    :param x:
    :return:
    """

    # vervangt spaties in zoektermen met '+' tekens
    x = str(x)
    x = re.sub(r'\s+', '+', x)

    #bouwt API-geaccepteerde url
    url = 'http://www.omdbapi.com/?'
    if x[:2] == 'tt':
        url += 'i=' + x
    else:
        url += 't=' + x

    #verbindt met API en extraheert gegevens, exceptions ingebouwd voor eventueel verbindingsverlies,
    # server- en client-side
    data = ''
    try:
        with urlopen(url) as f:
            data = f.read().decode()
        # # weergave raw data(debug)
        # print(data, '\n', '--', '\n')
    except error.HTTPError as H:
        print('server kan niet aan het verzoek voldoen.')
        print('Foutcode: ', H.code)
    except error.URLError as U:
        print('kan server niet bereiken.')
        print('Foutcode: ', U.code)


    #bouwt dictobject
    gegevens = literal_eval(data)
    #weergave dict(debug)
    # for key in gegevens:
    #     print(key, gegevens[key], '\n')
    return gegevens


#
# handmatige input(debug)
# print(APIrequest('robin hood'))


