import uuid
import datetime

class Toegangsbewijs:
    @classmethod
    def nieuw_toegangsbewijs_rnd(cls, gebruiker_id, film_id, starttijd):
        """ Maakt een toegangsbewijs met een random toegangscode. """
        return cls(cls.genereer_random_toegangs_id(), gebruiker_id, film_id, starttijd)

    @classmethod
    def nieuw_toegangsbewijs_str(cls, toegangscode, gebruiker_id, film_id, starttijd):
        """
        :param toegangscode: str
        :param gebruiker_id: str
        ;return Toegangsbewijs object

        Overige parameters zijn van hetzelfde type als __init__ aangeeft.
        """
        _toegangscode = cls.string_to_uuid(toegangscode)
        _gebruiker_id = cls.string_to_uuid(gebruiker_id)
        return cls(_toegangscode, _gebruiker_id, film_id, starttijd)

    @classmethod
    def genereer_random_toegangs_id(cls):
        """ Genereert een random toegangscode """
        return uuid.uuid4()

    @classmethod
    def string_to_uuid(cls, str_uuid):
        """ Converteer een string naar een uuid.UUID object. """
        return uuid.UUID(str_uuid)

    def __init__(self, toegangscode, gebruiker_id, film_id, starttijd):
        """
        :param toegangscode: uuid.UUID
        :param gebruiker_id: Gebruiker_id (BezoekerInfo.get_bezoeker_id()) (uuid.UUID)
        :param film_id: filmid van imdb (str)
        :param starttijd: starttijd (datetime object)
        """
        if type(toegangscode) is not uuid.UUID:
            raise TypeError("toegangscode moet een uuid.UUID object zijn.")
        if type(gebruiker_id) is not uuid.UUID:
            raise TypeError("gebruiker_id moet een uuid.UUID object zijn.")
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
