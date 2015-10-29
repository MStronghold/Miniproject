import uuid
from Loginsysteem import BezoekerInfo as _BezoekerInfo

class Toegangsbewijs:
    @classmethod
    def nieuw_toegangsbewijs_rnd(cls, gebruiker, film_id, starttijd, eindtijd):
        """ Maakt een toegangsbewijs met een random toegangscode. """
        return cls(gebruiker, cls.genereer_random_toegangs_id(), film_id, starttijd, eindtijd)

    @classmethod
    def genereer_random_toegangs_id(cls):
        """ Genereert een random toegangscode """
        return uuid.uuid4()

    def __init__(self, gebruiker, toegangscode, film_id, starttijd, eindtijd):
        """
        :param gebruiker: BezoekerInfo.BezoekerInfo
        :param toegangscode: uuid.UUID
        :param film_id: filmid van filmtotaal
        :param starttijd: starttijd in epoch
        :param eindtijd: eindtijd in epoch
        """
        if type(gebruiker) is not _BezoekerInfo.BezoekerInfo:
            raise TypeError("gebruiker moet een BezoekerInfo.BezoekerInfo object zijn.")
        if type(toegangscode) is not uuid.UUID:
            raise TypeError("toegangscode moet een uuid.UUID object zijn.")
        if type(film_id) is not int:
            raise TypeError("film_id moet een int zijn.")
        if type(starttijd) is not int or type(eindtijd) is not int:
            raise TypeError("starttijd en eindtijd moet int zijn.")

        self.__gebruiker = gebruiker
        self.__toegangscode = toegangscode
        self.__film_id = film_id
        self.__starttijd = starttijd
        self.__eindtijd = eindtijd

    def get_gebruiker(self):
        return self.__gebruiker

    def get_toegangscode(self):
        return self.__toegangscode

    def get_film_id(self):
        return self.__film_id

    def get_starttijd(self):
        return self.__starttijd

    def get_eindtijd(self):
        return self.__eindtijd
