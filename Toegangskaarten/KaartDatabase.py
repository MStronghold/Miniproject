import sqlite3
import uuid
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
            _database_connectie = sqlite3.connect("Kaarten.db")

        _cursor = _database_connectie.cursor()

        try:
            _cursor.execute("SELECT * FROM kaarten")
        except sqlite3.OperationalError:
            _cursor.execute("CREATE TABLE kaarten(gebruikerid TEXT, toegangscode TEXT, filmid TEXT, starttijd TEXT)")
            _database_connectie.commit()

        return _database_connectie

    @classmethod
    def kaart_opslaan(cls, toegangsbewijs):
        """
        :param toegangsbewijs: Toegangsbewijs object
        :return: True = gelukt, False = niet gelukt
        """
        if type(toegangsbewijs) is not _Toegangsbewijs.Toegangsbewijs:
            raise TypeError("toegangsbewijs moet een Toegangsbewijs object zijn.")

        _gebruikers_id = str(toegangsbewijs.get_gebruiker_id())
        _toegangscode = str(toegangsbewijs.get_toegangscode())
        _film_id = toegangsbewijs.get_film_id()
        _starttijd_obj = toegangsbewijs.get_starttijd()
        _starttijd_bin = pickle.dumps(_starttijd_obj)
        _starttijd_bin_str = ""
        for byte in _starttijd_bin:
            if _starttijd_bin_str == "":
                _starttijd_bin_str = str(byte)
            else:
                _starttijd_bin_str += "///" + str(byte)

        _query = "INSERT INTO kaarten (gebruikerid,toegangscode,filmid,starttijd) VALUES ('" + _gebruikers_id + "','" + _toegangscode + "','" + _film_id + "','" + _starttijd_bin_str + "')"
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
    def kaart_opvragen(cls, toegangscode):
        """
        :param toegangscode: uuid.UUID object of string met het UUID.
        :return: Toegangsbewijs object, of False als niets gevonden is.
        """
        if type(toegangscode) is not uuid.UUID or type(toegangscode) is not str:
            raise TypeError("toegangscode moet een uuid.UUID object zijn of een string.")

        _code = str(toegangscode)

        # s = dmp_str.split("///")
        # b = bytearray()
        #
        # for byte in s:
        #     b.append(int(byte))
        #
        # now2 = pickle.loads(b)

    @classmethod
    def kaarten_opvragen_gebruiker(cls, gebruiker_id):
        """
        :param gebruiker_id: uuid.UUID object of string met het UUID.
        :return: List met toegangskaarten bijbehorende aan het gebruiker_id, False als niets gevonden is.
        """
        if type(gebruiker_id) is not uuid.UUID or type(gebruiker_id) is not str:
            raise TypeError("gebruiker_id moet een uuid.UUID object zijn of een string.")

        _gebruiker_id = str(gebruiker_id)

    @classmethod
    def kaarten_opvragen_film(cls, film_id):
        """
        :param film_id: Het id van de film (string)
        :return: List met alle toegangskaarten uitgegeven voor de specifieke film_id.
        """
        if type(film_id) is not str:
            raise TypeError("film_id moet een string zijn.")

    @classmethod
    def kaart_verwijderen(cls, toegangscode):
        """
        :param toegangscode: uuid.UUID object of string met het UUID.
        :return: True als de toegangskaart verwijderd is, False als de toegangskaart niet gevonden kon worden.
        """
        if type(toegangscode) is not uuid.UUID or type(toegangscode) is not str:
            raise TypeError("toegangscode moet een uuid.UUID object zijn of een string.")
