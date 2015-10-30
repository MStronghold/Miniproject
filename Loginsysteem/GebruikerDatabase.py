import sqlite3
import uuid
from Loginsysteem import BezoekerInfo as _BezoekerInfo


class GebruikerDatabase:
    @classmethod
    def __verbind_met_database(cls):
        """
        :return: sqlite3.Connection, object waarmee er gelezen en geschreven kan worden naar de database.
        """
        try:
            _database_connectie = sqlite3.connect(".\Loginsysteem\Gebruikers.db")
        except sqlite3.OperationalError:
            try:
                _database_connectie = sqlite3.connect("..\Loginsysteem\Gebruikers.db")
            except sqlite3.OperationalError:
                _database_connectie = sqlite3.connect("Gebruikers.db")

        _cursor = _database_connectie.cursor()

        try:
            _cursor.execute("SELECT * FROM gebruikers")
        except sqlite3.OperationalError:
            _cursor.execute("CREATE TABLE gebruikers(ID TEXT, gebruikersnaam TEXT, email TEXT, wachtwoord TEXT, isaanbieder TEXT)")
            _database_connectie.commit()

        return _database_connectie

    @classmethod
    def gebruiker_opslaan(cls, gebruiker):
        """
        :param gebruiker: BezoekerInfo
        :return: bool, True als de gebruiker successvol opgeslagen is.
                       False als de gebruiker niet opgeslagen kon worden.
        """
        if type(gebruiker) is not _BezoekerInfo.BezoekerInfo:
            raise TypeError("Gebruiker moet een BezoekerInfo.BezoekerInfo object zijn.")

        # Unpack het BezoekerInfo object.
        _id = str(gebruiker.get_bezoeker_id())
        _gebruikersnaam = gebruiker.get_gebruikersnaam()
        _email = gebruiker.get_email()
        _wachtwoord = gebruiker.get_wachtwoord()
        _is_aanbieder = str(int(gebruiker.get_is_aanbieder()))

        # Bestaat de gebruiker al? Verwijder het dan.
        if cls.gebruiker_opvragen(_id):
            cls.gebruiker_verwijderen(_id, _type="ID")

        # Voorbereiding om de gebruiker op te slaan in de sqlite database.
        _query = "INSERT INTO gebruikers (ID,gebruikersnaam,email,wachtwoord,isaanbieder) VALUES ('" + _id + "','" + _gebruikersnaam + "','" + _email + "','" + _wachtwoord + "','" + _is_aanbieder + "')"
        _database_connectie = cls.__verbind_met_database()

        try:
            _database_connectie.cursor().execute(_query)
            return True
        except sqlite3.OperationalError:
            return False
        finally:
            _database_connectie.commit()
            _database_connectie.close()

    @classmethod
    def gebruiker_opvragen(cls, id):
        """
        :param id: str of uuid.UUID, het unieke ID van de gebruiker.
        :return: bool of BezoekerInfo, BezoekerInfo object als de gebruiker gevonden is.
                                       False als de gebruiker niet gevonden is.
        """
        if type(id) is not str and type(id) is not uuid.UUID:
            raise TypeError("id moet een string of een uuid.UUID object zijn.")

        # Database connectie en query voorbereiden.
        _query = "SELECT * FROM gebruikers"
        _database_connectie = cls.__verbind_met_database()

        # Gebruiker zoeken in de database.
        _id = str(id)
        for row in _database_connectie.cursor().execute(_query):
            if row[0] == _id or row[1] == _id or row[2] == _id:
                _b = _BezoekerInfo.BezoekerInfo.nieuw_bezoeker_str(row[0], row[1], row[2], row[3], bool(int(row[4])))
                _database_connectie.close()
                return _b
        _database_connectie.close()
        return False

    @classmethod
    def gebruiker_verwijderen(cls, id, _type=""):
        """
        :param id: str of uuid.UUID, het unieke ID van de gebruiker.
        :param _type: str, optioneel;
        :return: bool, True als de gebruiker is verwijderd.
                       False als de gebruiker niet gevonden is.
        """
        if type(id) is not str and type(id) is not uuid.UUID:
            raise TypeError("id moet een string of een uuid.UUID object zijn.")

        # Database connectie en query voorbereiden.
        _query = "SELECT * FROM gebruikers"
        _database_connectie = cls.__verbind_met_database()

        # Gebruiker zoeken in de database.
        _id = str(id)
        if not (_type == "ID" or _type == "gebruikersnaam" or _type == "email"):
            for row in _database_connectie.cursor().execute(_query):
                if row[0] == _id:
                    _type = "ID"
                    break
                elif row[1] == _id:
                    _type = "gebruikersnaam"
                    break
                elif row[2] == _id:
                    _type = "email"
                    break
                else:
                    _type = ""

        # Als de gebruiker gevonden is, verwijder het dan.
        if len(_type):
            _query_delete = "DELETE FROM gebruikers WHERE " + _type + " = '" + _id + "'"
            _database_connectie.cursor().execute(_query_delete)
            _database_connectie.commit()

        _database_connectie.close()

        return bool(len(_type))
