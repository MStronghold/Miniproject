import uuid
from Loginsysteem import BezoekerInfo as _BezoekerInfo
from Loginsysteem import GebruikerDatabase as _GebruikerDatabase

"""
    - Johan de Graaf, 30-10-2015
"""


class Login:

    # Tijdelijke opslag voor de BezoekerInfo objecten.
    __gebruikers = []

    @classmethod
    def gebruiker_opslaan(cls, gebruiker, forceer=False):
        """
        :param gebruiker: BezoekerInfo
        :return: int, 0 = Gebruiker aanmaken is niet gelukt (ID is al in gebruik).
                      1 = gebruikersnaam al in gebruik.
                      2 = Email al in gebruik.
                      3 = De gebruiker is successvol aangemaakt of gewijzigd.
        """

        if type(gebruiker) is not _BezoekerInfo.BezoekerInfo:
            raise TypeError("Gebruiker moet een BezoekerInfo.BezoekerInfo object zijn.")

        # Controleer of de gebruiker al bestaat in de database.
        if not forceer:
            if cls.gebruiker_opvragen(gebruiker.get_gebruikersnaam()):
                return 1
            elif cls.gebruiker_opvragen(gebruiker.get_email()):
                return 2

        # Verwijder de gebruiker uit de database (als deze al bestaat).
        if cls.gebruiker_opvragen(gebruiker.get_bezoeker_id()):
            cls.gebruiker_verwijderen(gebruiker.get_bezoeker_id())

        # Sla het BezoekerInfo object op in de tijdelijke opslag en sla het op in de database.
        cls.__gebruikers.append(gebruiker)
        if _GebruikerDatabase.GebruikerDatabase.gebruiker_opslaan(gebruiker):
            return 3
        else:
            return 0

    @classmethod
    def gebruiker_opvragen(cls, id):
        """
        :param id: str of uuid.UUID, het unieke ID van de gebruiker.
        :return: bool of BezoekerInfo, BezoekerInfo object als de gebruiker gevonden is.
                                       False als de gebruiker niet gevonden is.
        """
        if type(id) is not str and type(id) is not uuid.UUID:
            raise TypeError("id moet een string of een uuid.UUID object zijn.")

        # Gebruiker zoeken in de tijdelijke opslag.
        _id = str(id)
        for i in cls.__gebruikers:
            if i.get_bezoeker_id() == _id or i.get_gebruikersnaam() == _id or i.get_email() == _id:
                return i

        # Als de gebruiker niet gevonden is in de tijdelijke opslag,
        #   zoek het dan op in de database en voeg het toe aan de tijdelijke opslag.
        _b = _GebruikerDatabase.GebruikerDatabase.gebruiker_opvragen(id)
        if _b:
            cls.__gebruikers.append(_b)

        return _b

    @classmethod
    def gebruiker_verwijderen(cls, id):
        """
        :param id: str of uuid.UUID, het unieke ID van de gebruiker.
        :return: bool, True als de gebruiker is verwijderd.
                       False als de gebruiker niet gevonden is.
        """
        if type(id) is not str and type(id) is not uuid.UUID:
            raise TypeError("id moet een string of een uuid.UUID object zijn.")

        # Gebruiker zoeken in de tijdelijke opslag en daaruit verwijderen.
        _id = str(id)
        for i in cls.__gebruikers:
            if str(i.get_bezoeker_id()) == _id or i.get_gebruikersnaam() == _id or i.get_email() == _id:
                del cls.__gebruikers[cls.__gebruikers.index(i)]

        # Gebruiker zoeken in de database en daaruit verwijderen.
        return _GebruikerDatabase.GebruikerDatabase.gebruiker_verwijderen(id)
