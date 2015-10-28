import uuid
from Loginsysteem import BezoekerInfo as _BezoekerInfo
from Loginsysteem import GebruikerDatabase as _GebruikerDatabase


class Login:

    __gebruikers = []

    @classmethod
    def gebruiker_opslaan(cls, gebruiker, forceer=False):
        """
        :param gebruiker: Gebruiker (BezoekerInfo object)
        :return: 0 = Gebruiker aanmaken is niet gelukt.
                 1 = gebruikersnaam al in gebruik.
                 2 = Email al in gebruik.
                 3 = De gebruiker is successvol aangemaakt of gewijzigd.
        """

        if type(gebruiker) is not _BezoekerInfo.BezoekerInfo:
            raise TypeError("Gebruiker moet een BezoekerInfo.BezoekerInfo object zijn.")

        if not forceer:
            if cls.gebruiker_opvragen(gebruiker.get_gebruikersnaam()):
                return 1
            elif cls.gebruiker_opvragen(gebruiker.get_email()):
                return 2

        if cls.gebruiker_opvragen(gebruiker.get_bezoeker_id()):
            cls.gebruiker_verwijderen(gebruiker.get_bezoeker_id())

        cls.__gebruikers.append(gebruiker)
        if _GebruikerDatabase.GebruikerDatabase.gebruiker_opslaan(gebruiker):
            return 3
        else:
            return 0

    @classmethod
    def gebruiker_opvragen(cls, id):
        """
        :param id: ID, gebruikersnaam of email.
        :return: BezoekerInfo object als de gebruiker gevonden is, False als de gebruiker niet gevonden is.
        """
        if type(id) is not str and type(id) is not uuid.UUID:
            raise TypeError("id moet een string of een uuid.UUID object zijn.")

        _id = str(id)
        for i in cls.__gebruikers:
            if i.get_bezoeker_id() == _id or i.get_gebruikersnaam() == _id or i.get_email() == _id:
                return i

        _b = _GebruikerDatabase.GebruikerDatabase.gebruiker_opvragen(id)
        if _b:
            cls.__gebruikers.append(_b)

        return _b

    @classmethod
    def gebruiker_verwijderen(cls, id):
        """
        :param id: ID, gebruikersnaam of email.
        :return: True als de gebruiker verwijderd is, False als de gebruiker niet gevonden is of niet verwijderd kon worden.
        """
        if type(id) is not str and type(id) is not uuid.UUID:
            raise TypeError("id moet een string of een uuid.UUID object zijn.")

        _id = str(id)
        for i in cls.__gebruikers:
            if str(i.get_bezoeker_id()) == _id or i.get_gebruikersnaam() == _id or i.get_email() == _id:
                del cls.__gebruikers[cls.__gebruikers.index(i)]

        return _GebruikerDatabase.GebruikerDatabase.gebruiker_verwijderen(id)
