import uuid

"""
    - Johan de Graaf, 30-10-2015
"""


class BezoekerInfo:
    @classmethod
    def genereer_random_bezoeker_id(cls):
        """
        Genereer een random uuid.
        :return: uuid.UUID
        """
        return uuid.uuid4()

    @classmethod
    def string_to_uuid(cls, str_uuid):
        """
        Converteer een string naar een uuid.UUID object.
        :param str_uuid: str, het unieke bezoekers ID.
        :return: uuid.UUID
        """
        return uuid.UUID(str_uuid)

    @classmethod
    def nieuw_bezoeker_rnd(cls, gebruikersnaam, email, wachtwoord, is_aanbieder=False):
        """
        Maak een BezoekerInfo object met een random uuid.
        :param gebruikersnaam: str, de gebruikersnaam van de bezoeker.
        :param email: str, het emailadres van de bezoeker.
        :param wachtwoord: str, het wachtwoord van de bezoeker.
        :param is_aanbieder: bool, geeft aan of de bezoeker een aanbieder is.
        :return: BezoekerInfo
        """
        return cls(cls.genereer_random_bezoeker_id(), gebruikersnaam, email, wachtwoord, is_aanbieder)

    @classmethod
    def nieuw_bezoeker_str(cls, str_uuid, gebruikersnaam, email, wachtwoord, is_aanbieder=False):
        """ Maak een BezoekerInfo object met uuid als string. """
        return cls(cls.string_to_uuid(str_uuid), gebruikersnaam, email, wachtwoord, is_aanbieder)

    def __init__(self, bezoeker_id, gebruikersnaam, email, wachtwoord, is_aanbieder=False):
        """
        :param bezoeker_id: uuid.UUID, dit moet uniek zijn voor elke bezoeker.
        :param gebruikersnaam: str, de gebruikersnaam van de bezoeker.
        :param email: str, het emailadres van de bezoeker.
        :param wachtwoord: str, het wachtwoord van de bezoeker.
        :param is_aanbieder: bool, geeft aan of de gebruiker een aanbieder is.
        :return: BezoekerInfo
        """

        if type(bezoeker_id) is not uuid.UUID:
            raise TypeError("bezoeker_id moet een uuid.UUID object zijn.")
        if type(gebruikersnaam) is not str:
            raise TypeError("gebruikersnaam moet een str zijn.")
        if type(email) is not str:
            raise TypeError("email moet een str zijn.")
        if type(wachtwoord) is not str:
            raise TypeError("wachtwoord moet een str zijn.")
        if type(is_aanbieder) is not bool:
            raise TypeError("is_aanbieder moet een bool zijn.")

        self.__bezoeker_id = bezoeker_id
        self.__gebruikersnaam = gebruikersnaam
        self.__email = email
        self.__wachtwoord = wachtwoord
        self.__is_aanbieder = is_aanbieder

    def to_dict(self):
        """
        :return: dict, Zet het BezoekerInfo object om naar een dictionary.
        """
        return {"ID" : self.get_bezoeker_id(), "gebruikersnaam" : self.get_gebruikersnaam(), "email" : self.get_email(), "wachtwoord" : self.get_wachtwoord(), "isaanbieder" : self.get_is_aanbieder()}

    def get_bezoeker_id(self):
        """
        :return: uuid.UUID, haal het unieke id van de bezoeker op.
        """
        return self.__bezoeker_id

    def get_gebruikersnaam(self):
        """
        :return: string, haal de gebruikersnaam van de bezoeker op.
        """
        return self.__gebruikersnaam

    def get_email(self):
        """
        :return: string, haal het emailadres van de bezoeker op
        """
        return self.__email

    def get_wachtwoord(self):
        """
        :return: string, haal het wachtwoord van de bezoeker op.
        """
        return self.__wachtwoord

    def get_is_aanbieder(self):
        """
        :return: bool, is de bezoeker een aanbieder?
        """
        return self.__is_aanbieder

    def set_gebruikersnaam(self, gebruikersnaam):
        """
        :param gebruikersnaam: string, verander de gebruikersnaam van de bezoeker.
        """
        if type(gebruikersnaam) is not str:
            raise TypeError("gebruikersnaam moet een str zijn.")

        self.__gebruikersnaam = gebruikersnaam

    def set_email(self, email):
        """
        :param email: string, verander het emailadres van de bezoeker.
        """
        if type(email) is not str:
            raise TypeError("email moet een str zijn.")

        self.__email = email

    def set_wachtwoord(self, wachtwoord):
        """
        :param wachtwoord: string, verander het wachtwoord van de bezoeker.
        """
        if type(wachtwoord) is not str:
            raise TypeError("wachtwoord moet een str zijn.")

        self.__wachtwoord = wachtwoord

    def set_is_aanbieder(self, is_aanbieder):
        """
        :param is_aanbieder: bool, verander of de bezoeker een aanbieder is.
        """
        if type(is_aanbieder) is not bool:
            raise TypeError("is_aanbieder moet een bool zijn.")

        self.__is_aanbieder = is_aanbieder
