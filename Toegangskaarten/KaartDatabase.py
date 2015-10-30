import sqlite3
import uuid
import datetime
import pickle
from Toegangskaarten import Toegangsbewijs as _Toegangsbewijs

"""
    - Johan de Graaf, 30-10-2015
"""


class KaartDatabase:
    @classmethod
    def __verbind_met_database(cls):
        """
        :return: sqlite3.Connection, object waarmee er gelezen en geschreven kan worden naar de database.
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
        Zet een datetime object om naar een string.
        :param datetime_obj: datetime, het datetime object wat geencodeerd moet worden naar een string.
        :return: string, de string waarin het datetime object geencodeerd in opgeslagen zit.
        """
        if type(datetime_obj) is not datetime.datetime:
            raise TypeError("datetime_obj moet een datetime object zijn.")

        _datetime_bin = pickle.dumps(datetime_obj)          # Maak een bytes() van het datetime object.
        _datetime_bin_str = ""
        for byte in _datetime_bin:                          # Converteer het bytes() naar een string.
            if _datetime_bin_str == "":
                _datetime_bin_str = str(byte)
            else:
                _datetime_bin_str += "///" + str(byte)

        return _datetime_bin_str

    @classmethod
    def __string_to_datetime(cls, datetime_str):
        """
        Zet een string om naar een datetime object.
        :param datetime_str: str, de string waarin het datetime object geencodeerd in opgeslagen zit.
        :return: bool of datetime, datetime = De string kon omgezet worden naar een datetime object
                                   False = De string kon niet omgezet worden naar een datetime object.
        """

        if type(datetime_str) is not str:
            raise TypeError("datetime_str moet string zijn zijn.")

        _datetime_bin_str_list = datetime_str.split("///")  # Verdeel de string naar een list, de elementen zijn van het type str.
        _datetime_bin = bytearray()

        for byte in _datetime_bin_str_list:                 # Zet elk element in de lijst om naar een int, en stop dit in de bytearray().
            _datetime_bin.append(int(byte))

        _datetime_obj = None

        try:
            _datetime_obj = pickle.loads(_datetime_bin)     # Decodeer de bytearray() terug naar het oorspronkelijke datetime object.
        except BaseException:
            _datetime_obj = False

        return _datetime_obj

    @classmethod
    def kaart_opslaan(cls, toegangsbewijs, forceer=False):
        """
        Sla een kaart op in de database.
        :param toegangsbewijs: Toegangsbewijs, het toegangsbewijs dat moet worden opgeslagen in de database.
        :param forceer: bool, False = Als de gebruiker al bestaat in de database wordt er niks opgeslagen.
                              True  = Als de gebruiker al bestaat in de database wordt deze overschreven.
        :return: bool, False = Kaart opslaan is niet gelukt. (de toegangscode is al in gebruik)
                       True = De kaart is successvol aangemaakt of gewijzigd.
        """
        if type(toegangsbewijs) is not _Toegangsbewijs.Toegangsbewijs:
            raise TypeError("toegangsbewijs moet een Toegangsbewijs object zijn.")

        _toegangscode = str(toegangsbewijs.get_toegangscode())

        # Controleer of de gebruiker al in de database staat.
        if cls.kaart_opvragen(_toegangscode):
            if forceer:
                cls.kaart_verwijderen(_toegangscode)
            else:
                return False

        # Unpack het toegangsbewijs object.
        _gebruikers_id = str(toegangsbewijs.get_gebruiker_id())
        _film_id = toegangsbewijs.get_film_id()
        _starttijd_bin_str = cls.__datetime_to_string(toegangsbewijs.get_starttijd())

        # Voorbereiding om de toegangskaart op te slaan in de database.
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
        Kaart opvragen uit de database.
        :param toegangscode: uuid.UUID of str, het unieke ID van het toegangsbewijs.
        :return: Toegangsbewijs of bool, Toegangsbewijs = de kaart is gevonden in de database.
                                         False = de kaart is niet gevonden in de database.
        """
        if type(toegangscode) is not uuid.UUID and type(toegangscode) is not str:
            raise TypeError("toegangscode moet een uuid.UUID object zijn of een string.")

        # Voorbereiding om de toegangskaart op te vragen uit de database.
        _query = "SELECT * FROM kaarten"
        _database_connectie = cls.__verbind_met_database()

        _code = str(toegangscode)

        _toegangscode = ""
        _gebruikers_id = ""
        _film_id = ""
        _starttijd_obj = None

        # Database doorzoeken naar het toegangsbewijs
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
        Kaarten zoeken op gebruikersid.
        :param gebruiker_id: uuid.UUID of str, het unieke ID van de gebruiker.
        :return: List(Toegangsbewijs) of bool, List(Toegangsbewijs) = er zijn toegangsbewijzen gevonden.
                                               False = er zijn geen toegangsbewijzen gevonden.
        """
        if type(gebruiker_id) is not uuid.UUID and type(gebruiker_id) is not str:
            raise TypeError("gebruiker_id moet een uuid.UUID object zijn of een string.")

        _gebruiker_id = str(gebruiker_id)

        # Voorbereiding om de toegangskaarten op te vragen uit de database.
        _query = "SELECT * FROM kaarten"
        _database_connectie = cls.__verbind_met_database()

        _kaarten_gebruiker = []

        # Zoek de toegangskaarten behorende aan het gebruiker_id
        for row in _database_connectie.cursor().execute(_query):
            if row[1] == _gebruiker_id:
                _kaarten_gebruiker.append(_Toegangsbewijs.Toegangsbewijs.nieuw_toegangsbewijs_str(row[0], row[1], row[2], cls.__string_to_datetime(row[3])))

        _database_connectie.close()
        return _kaarten_gebruiker if len(_kaarten_gebruiker) else bool(len(_kaarten_gebruiker))

    @classmethod
    def kaarten_opvragen_film(cls, film_id):
        """
        Kaarten zoeken op film_id.
        :param film_id: str, het IMDB id van de film.
        :return: List(Toegangsbewijs) of bool, List(Toegangsbewijs) = er zijn toegangsbewijzen gevonden.
                                               False = er zijn geen toegangsbewijzen gevonden.
        """
        if type(film_id) is not str:
            raise TypeError("film_id moet een string zijn.")

        # Voorbereiding om de toegangskaarten op te vragen uit de database.
        _query = "SELECT * FROM kaarten"
        _database_connectie = cls.__verbind_met_database()

        _kaarten_film = []

        # Zoek de toegangskaarten behorende aan het film_id
        for row in _database_connectie.cursor().execute(_query):
            if row[2] == film_id:
                _kaarten_film.append(_Toegangsbewijs.Toegangsbewijs.nieuw_toegangsbewijs_str(row[0], row[1], row[2], cls.__string_to_datetime(row[3])))

        _database_connectie.close()
        return _kaarten_film if len(_kaarten_film) else bool(len(_kaarten_film))

    @classmethod
    def kaart_verwijderen(cls, toegangscode):
        """
        Kaarten verwijderen uit de database.
        :param toegangscode: uuid.UUID of str, het unieke ID van het toegangsbewijs.
        :return: bool, True = de toegangskaart is successvol verwijderd uit de database.
                       False = de toegangskaart kon niet gevonden worden in de database.
        """
        if type(toegangscode) is not uuid.UUID and type(toegangscode) is not str:
            raise TypeError("toegangscode moet een uuid.UUID object zijn of een string.")

        _toegangscode = str(toegangscode)

        # Voorbereiding om de toegangskaarten op te vragen uit de database, en te verwijderen.
        _query = "SELECT * FROM kaarten"
        _query_delete = "DELETE FROM kaarten WHERE " + "toegangscode" + " = '" + _toegangscode + "'"
        _database_connectie = cls.__verbind_met_database()

        # Controleert of de toegangskaart wel voorkomt in de database.
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
