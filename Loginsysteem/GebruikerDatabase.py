import sqlite3
import uuid
from Loginsysteem import BezoekerInfo as _BezoekerInfo


class GebruikerDatabase:

    @classmethod
    def __verbind_met_database(cls):
        """
        :return: sqlite3.Connection
        """
        try:
            _database_connectie = sqlite3.connect(".\Loginsysteem\Gebruikers.db")
        except sqlite3.OperationalError:
            _database_connectie = sqlite3.connect("Gebruikers.db")

        _cursor = _database_connectie.cursor()

        try:
            _cursor.execute("SELECT * FROM gebruikers")
        except sqlite3.OperationalError:
            _cursor.execute("CREATE TABLE gebruikers(ID TEXT, gebruikersnaam TEXT, email TEXT, wachtwoord TEXT)")
            _database_connectie.commit()

        return _database_connectie

    @classmethod
    def gebruiker_opslaan(cls, gebruiker):
        if type(gebruiker) is not _BezoekerInfo.BezoekerInfo:
            raise TypeError("Gebruiker moet een BezoekerInfo.BezoekerInfo object zijn.")

        _id = str(gebruiker.get_bezoeker_id())
        _gebruikersnaam = gebruiker.get_gebruikersnaam()
        _email = gebruiker.get_email()
        _wachtwoord = gebruiker.get_wachtwoord()

        if cls.gebruiker_opvragen(_id):
            cls.gebruiker_verwijderen(_id, _type="ID")

        _query = "INSERT INTO gebruikers (ID,gebruikersnaam,email,wachtwoord) VALUES ('" + _id + "','" + _gebruikersnaam + "','" + _email + "','" + _wachtwoord + "')"
        _database_connectie = cls.__verbind_met_database()

        _gelukt = None
        try:
            _database_connectie.cursor().execute(_query)
            _gelukt = True
        except:
            _gelukt = False
        finally:
            _database_connectie.commit()
            _database_connectie.close()

        return _gelukt

    @classmethod
    def gebruiker_opvragen(cls, id):
        if type(id) is not str and type(id) is not uuid.UUID:
            raise TypeError("id moet een string of een uuid.UUID object zijn.")

        _query = "SELECT * FROM gebruikers"
        _database_connectie = cls.__verbind_met_database()

        _id = str(id)
        for row in _database_connectie.cursor().execute(_query):
            if row[0] == _id or row[1] == _id or row[2] == _id:
                return _BezoekerInfo.BezoekerInfo.nieuw_bezoeker_str(row[0], row[1], row[2], row[3])
        return False

    @classmethod
    def gebruiker_verwijderen(cls, id, _type=""):
        if type(id) is not str and type(id) is not uuid.UUID:
            raise TypeError("id moet een string of een uuid.UUID object zijn.")

        _query = "SELECT * FROM gebruikers"
        _database_connectie = cls.__verbind_met_database()

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

        if len(_type):
            _query_delete = "DELETE FROM gebruikers WHERE " + _type + " = '" + _id + "'"
            _database_connectie.cursor().execute(_query_delete)
            _database_connectie.commit()

        _database_connectie.close()

        return id if bool(len(_type)) else bool(len(_type))
