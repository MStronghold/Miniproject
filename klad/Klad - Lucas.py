from urllib.request import urlopen      #http connector
from urllib import error                #error handling
from ast import literal_eval            #dict naar string converter
import re                               #regular expressions voor url-opbouw en filtering
import json


def APIrequest(x, search=0):
    """
    Invoerfunctie voor zoekveld.
    Accepteert string(titel of idnummer),
    vraagt info en returned een dict met informatie.
    :param x=str:
    :return:
    """

    # vervangt spaties in zoektermen met '+' tekens
    x = str(x)
    x = re.sub(r'\s+', '+', x)

    #bouwt API-geaccepteerde url
    url = 'http://www.omdbapi.com/?'
    if search==1:
        url += 's=' + x
        print(url)
    elif x[:2] == 'tt':
        url += 'i=' + x
    else:
        url += 't=' + x

    #verbindt met API en extraheert gegevens, exceptions ingebouwd voor eventueel verbindingsverlies,
    # server- en client-side
    try:
        with urlopen(url) as f:
            data = f.read().decode()
        # weergave raw data(debug)
        print(data, '\n', '--', '\n')
    except error.HTTPError as H:
        print('server kan niet aan het verzoek voldoen.')
        print('Foutcode: ', H.code)
    except error.URLError as U:
        print('kan server niet bereiken.')
        print('Foutcode: ', U.code)

    # print('data pre: ' + data)
    # data = data.replace('{"Search":[', '')
    # data = data.replace(']}', '')
    print('data post: ' + str(type(data)) + '\n' + str(data))
    #bouwt dictobject
    json_string = data
    gegevens = json.loads(json_string)
    # gegevens[regel[0]] = regel[1]
    # gegevens = literal_eval(data)



    #weergave dict(debug)
    # for key in gegevens:
    #     print(key, gegevens[key], '\n')
    try:
        if search==1:
            print('Zoekresultaten:', '\n')
            print(gegevens)
        elif gegevens['Response'] == 'False':
            APIrequest(x, search=1)
            print('check tail', '\n')
    except (KeyError):
        return gegevens
    return gegevens




#handmatige input(debug)
APIrequest('star wars')
