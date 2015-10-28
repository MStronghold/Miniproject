import uuid


class BezoekerInfo:
    @classmethod
    def genereer_random_bezoeker_id(cls):
        return uuid.uuid4()

    @classmethod
    def string_to_uuid(cls, str_uuid):
        return uuid.UUID(str_uuid)

    @classmethod
    def nieuw_bezoeker_rnd(cls, gebruikersnaam, email, wachtwoord):
        return cls(cls.genereer_random_bezoeker_id(), gebruikersnaam, email, wachtwoord)

    @classmethod
    def nieuw_bezoeker_str(cls, str_uuid, gebruikersnaam, email, wachtwoord):
        return cls(cls.string_to_uuid(str_uuid), gebruikersnaam, email, wachtwoord)

    def __init__(self, bezoeker_id, gebruikersnaam, email, wachtwoord):
        """
        :param bezoeker_id: uuid.UUID
        :param naam:  str
        :param email:  str
        :param wachtwoord: str
        """

        if type(bezoeker_id) is not uuid.UUID:
            raise TypeError("bezoeker_id moet een uuid.UUID object zijn.")
        if type(gebruikersnaam) is not str:
            raise TypeError("gebruikersnaam moet een str zijn.")
        if type(email) is not str:
            raise TypeError("email moet een str zijn.")
        if type(wachtwoord) is not str:
            raise TypeError("wachtwoord moet een str zijn.")

        self.__bezoeker_id = bezoeker_id
        self.__gebruikersnaam = gebruikersnaam
        self.__email = email
        self.__wachtwoord = wachtwoord

    def to_dict(self):
        return {"ID" : self.get_bezoeker_id(), "gebruikersnaam" : self.get_gebruikersnaam(), "email" : self.get_email(), "wachtwoord" : self.get_wachtwoord()}

    def get_bezoeker_id(self):
        return self.__bezoeker_id

    def get_gebruikersnaam(self):
        return self.__gebruikersnaam

    def get_email(self):
        return self.__email

    def get_wachtwoord(self):
        return self.__wachtwoord

    def set_gebruikersnaam(self, gebruikersnaam):
        self.__gebruikersnaam = gebruikersnaam

    def set_email(self, email):
        self.__email = email

    def set_wachtwoord(self, wachtwoord):
        self.__wachtwoord = wachtwoord
