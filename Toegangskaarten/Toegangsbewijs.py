import uuid
import datetime

class Toegangsbewijs:
    @classmethod
    def nieuw_toegangsbewijs_rnd(cls, gebruiker_id, film_id, starttijd):
        """ Maakt een toegangsbewijs met een random toegangscode. """
        return cls(cls.genereer_random_toegangs_id(), gebruiker_id, film_id, starttijd)

    @classmethod
    def genereer_random_toegangs_id(cls):
        """ Genereert een random toegangscode """
        return uuid.uuid4()

    def __init__(self, toegangscode, gebruiker_id, film_id, starttijd):
        """
        :param toegangscode: uuid.UUID
        :param gebruiker_id: Gebruiker_id (BezoekerInfo.get_bezoeker_id()) (uuid.UUID)
        :param film_id: filmid van imdb (str)
        :param starttijd: starttijd (datetime object)
        """
        if type(gebruiker_id) is not uuid.UUID:
            raise TypeError("gebruiker_id moet een uuid.UUID object zijn.")
        if type(toegangscode) is not uuid.UUID:
            raise TypeError("toegangscode moet een uuid.UUID object zijn.")
        if type(film_id) is not str:
            raise TypeError("film_id moet een str zijn.")
        if type(starttijd) is not datetime.datetime:
            raise TypeError("starttijd moet een datetime object zijn.")

        self.__toegangscode = toegangscode
        self.__gebruiker_id = gebruiker_id
        self.__film_id = film_id
        self.__starttijd = starttijd

    def get_toegangscode(self):
        return self.__toegangscode

    def get_gebruiker_id(self):
        return self.__gebruiker_id

    def get_film_id(self):
        return self.__film_id

    def get_starttijd(self):
        return self.__starttijd
