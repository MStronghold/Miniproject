import sqlite3
import uuid
import datetime
import pickle
from Toegangskaarten import Toegangsbewijs as _Toegangsbewijs


class KaartDatabase:
    @classmethod
    def __verbind_met_database(cls):
        """
        :return: sqlite3.Connection
        """
        try:
            _database_connectie = sqlite3.connect(".\Toegangskaarten\Kaarten.db")
        except sqlite3.OperationalError:
            try:
                _database_connectie = sqlite3.connect("..\Toegangskaarten\Kaarten.db")
            except sqlite3.OperationalError:
                _database_connectie = sqlite3.connect("Kaarten.db")

        _cursor = _database_connectie.cursor()

        try:
            _cursor.execute("SELECT * FROM kaarten")
        except sqlite3.OperationalError:
            _cursor.execute("CREATE TABLE kaarten(toegangscode TEXT, gebruikerid TEXT, filmid TEXT, starttijd TEXT)")
            _database_connectie.commit()

        return _database_connectie

    @classmethod
    def __datetime_to_string(cls, datetime_obj):
        """
        :param datetime_obj: datetime.datetime object
        :return: string
        """
        if type(datetime_obj) is not datetime.datetime:
            raise TypeError("datetime_obj moet een datetime object zijn.")

        _datetime_bin = pickle.dumps(datetime_obj)
        _datetime_bin_str = ""
        for byte in _datetime_bin:
            if _datetime_bin_str == "":
                _datetime_bin_str = str(byte)
            else:
                _datetime_bin_str += "///" + str(byte)

        return _datetime_bin_str

    @classmethod
    def __string_to_datetime(self, datetime_str):
        """
        :param datetime_str: string
        :return: datetime object of False als het niet gelukt is.
        """

        if type(datetime_str) is not datetime.datetime:
            raise TypeError("datetime_str moet een string zijn.")

        _datetime_bin_str_list = datetime_str.split("///")
        _datetime_bin = bytearray()

        for byte in _datetime_bin_str_list:
            _datetime_bin.append(int(byte))

        _datetime_obj = None

        try:
            _datetime_obj = pickle.loads(_datetime_bin)
        except BaseException:
            return False

        return _datetime_obj if type(_datetime_obj) == datetime.datetime else False

    @classmethod
    def kaart_opslaan(cls, toegangsbewijs, forceer=False):
        """
        :param toegangsbewijs: Toegangsbewijs object
        :return: False = Kaart opslaan is niet gelukt. (de toegangscode is al in gebruik)
                 True = De kaart is successvol aangemaakt of gewijzigd.
        """
        if type(toegangsbewijs) is not _Toegangsbewijs.Toegangsbewijs:
            raise TypeError("toegangsbewijs moet een Toegangsbewijs object zijn.")

        _toegangscode = str(toegangsbewijs.get_toegangscode())

        if cls.kaart_opvragen(_toegangscode):
            if forceer:
                cls.kaart_verwijderen(_toegangscode)
            else:
                return False

        _gebruikers_id = str(toegangsbewijs.get_gebruiker_id())
        _film_id = toegangsbewijs.get_film_id()
        _starttijd_bin_str = cls.__datetime_to_string(toegangsbewijs.get_starttijd())

        _query = "INSERT INTO kaarten (toegangscode,gebruikerid,filmid,starttijd) VALUES ('" + _toegangscode + "','" + _gebruikers_id + "','" + _film_id + "','" + _starttijd_bin_str + "')"
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
    def kaart_opvragen(cls, toegangscode):
        """
        :param toegangscode: uuid.UUID object of string met het UUID.
        :return: Toegangsbewijs object, of False als niets gevonden is.
        """
        if type(toegangscode) is not uuid.UUID and type(toegangscode) is not str:
            raise TypeError("toegangscode moet een uuid.UUID object zijn of een string.")

        _query = "SELECT * FROM kaarten"
        _database_connectie = cls.__verbind_met_database()

        _code = str(toegangscode)

        _toegangscode = ""
        _gebruikers_id = ""
        _film_id = ""
        _starttijd_obj = None

        for row in _database_connectie.cursor().execute(_query):
            if row[0] == _code:
                _toegangscode = row[0]
                _gebruikers_id = row[1]
                _film_id = row[2]
                _starttijd_obj = cls.__string_to_datetime(row[3])
                break

        _database_connectie.close()
        return False if not _starttijd_obj else _Toegangsbewijs.Toegangsbewijs.nieuw_toegangsbewijs_str(_toegangscode, _gebruikers_id, _film_id, _starttijd_obj)

    @classmethod
    def kaarten_opvragen_gebruiker(cls, gebruiker_id):
        """
        :param gebruiker_id: uuid.UUID object of string met het UUID.
        :return: List met toegangskaarten bijbehorende aan het gebruiker_id, False als niets gevonden is.
        """
        if type(gebruiker_id) is not uuid.UUID or type(gebruiker_id) is not str:
            raise TypeError("gebruiker_id moet een uuid.UUID object zijn of een string.")

        _gebruiker_id = str(gebruiker_id)

        _query = "SELECT * FROM kaarten"
        _database_connectie = cls.__verbind_met_database()

        _kaarten_gebruiker = []

        for row in _database_connectie.cursor().execute(_query):
            if row[1] == _gebruiker_id:
                _kaarten_gebruiker.append(_Toegangsbewijs.Toegangsbewijs.nieuw_toegangsbewijs_str(row[0], row[1], row[2], cls.__string_to_datetime(row[3])))

        _database_connectie.close()
        return _kaarten_gebruiker if len(_kaarten_gebruiker) else bool(len(_kaarten_gebruiker))

    @classmethod
    def kaarten_opvragen_film(cls, film_id):
        """
        :param film_id: Het id van de film (string)
        :return: List met alle toegangskaarten uitgegeven voor de specifieke film_id.
        """
        if type(film_id) is not str:
            raise TypeError("film_id moet een string zijn.")

        _query = "SELECT * FROM kaarten"
        _database_connectie = cls.__verbind_met_database()

        _kaarten_film = []

        for row in _database_connectie.cursor().execute(_query):
            if row[2] == film_id:
                _kaarten_film.append(_Toegangsbewijs.Toegangsbewijs.nieuw_toegangsbewijs_str(row[0], row[1], row[2], cls.__string_to_datetime(row[3])))

        _database_connectie.close()
        return _kaarten_film if len(_kaarten_film) else bool(len(_kaarten_film))

    @classmethod
    def kaart_verwijderen(cls, toegangscode):
        """
        :param toegangscode: uuid.UUID object of string met het UUID.
        :return: True als de toegangskaart verwijderd is, False als de toegangskaart niet gevonden kon worden.
        """
        if type(toegangscode) is not uuid.UUID or type(toegangscode) is not str:
            raise TypeError("toegangscode moet een uuid.UUID object zijn of een string.")

        _toegangscode = str(toegangscode)

        _query = "SELECT * FROM kaarten"
        _query_delete = "DELETE FROM kaarten WHERE " + "toegangscode" + " = '" + _toegangscode + "'"
        _database_connectie = cls.__verbind_met_database()

        _in_database = False
        for row in _database_connectie.cursor().execute(_query):
            if row[0] == _toegangscode:
                _in_database = True
                break

        if _in_database:
            _database_connectie.cursor().execute(_query_delete)

        _database_connectie.commit()
        _database_connectie.close()

        return _in_database
