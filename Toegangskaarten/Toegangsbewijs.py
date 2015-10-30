import uuid
import datetime
import qrcode as _qrcode

"""
    - Johan de Graaf, 30-10-2015
"""


class Toegangsbewijs:
    @classmethod
    def nieuw_toegangsbewijs_rnd(cls, gebruiker_id, film_id, starttijd):
        """
        Maakt een toegangsbewijs met een random toegangscode.
        :param gebruiker_id: uuid.UUID, het unieke ID van de gebruiker.
        :param film_id: str, het IMDB id van de film.
        :param starttijd: datetime, de starttijd van de film.
        :return: Toegangsbewijs
        """
        return cls(cls.genereer_random_toegangs_id(), gebruiker_id, film_id, starttijd)

    @classmethod
    def nieuw_toegangsbewijs_str(cls, toegangscode, gebruiker_id, film_id, starttijd):
        """
        :param toegangscode: str, dit moet uniek zijn voor elk Toegangsbewijs.
        :param gebruiker_id: str, het unieke ID van de gebruiker.
        :param film_id: str, het IMDB id van de film.
        :param starttijd: datetime, de starttijd van de film.
        :return: Toegangsbewijs
        """
        _toegangscode = cls.string_to_uuid(toegangscode)
        _gebruiker_id = cls.string_to_uuid(gebruiker_id)
        return cls(_toegangscode, _gebruiker_id, film_id, starttijd)

    @classmethod
    def genereer_random_toegangs_id(cls):
        """
        Genereer een random uuid.
        :return: uuid.UUID
        """
        return uuid.uuid4()

    @classmethod
    def string_to_uuid(cls, str_uuid):
        """
        Converteer een string naar een uuid.UUID object.
        :param str_uuid: str
        :return: uuid.UUID
        """
        return uuid.UUID(str_uuid)

    def __init__(self, toegangscode, gebruiker_id, film_id, starttijd):
        """
        :param toegangscode: uuid.UUID, dit moet uniek zijn voor elk Toegangsbewijs.
        :param gebruiker_id: uuid.UUID, het unieke ID van de gebruiker.
        :param film_id: str, het IMDB id van de film.
        :param starttijd: datetime, de starttijd van de film.
        :return: Toegangsbewijs
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

    def genereer_qr(self, path=""):
        """
        :param path: str, optioneel; het pad waar de QR afbeelding opgeslagen zal worden.
        :return: pil.PilImage of bool, Als path niet opgegeven is: pil.PilImage object
                                       Als path opgegeven is: True als de afbeelding successvol is opgeslagen.
                                                              False als er iets fout gegaan is tijdens het opslaan.
        """
        # De qrcode aanmaken (pil.PiLImage object)
        _qr = _qrcode.QRCode(version=1, error_correction=_qrcode.ERROR_CORRECT_M)
        _qr.add_data(str(self.get_toegangscode()))
        _qr.make()
        _qr_img = _qr.make_image()

        if path is "":
            return _qr_img
        else:
            try:
                _qr_img.save(path)
                return True
            except:
                return False

    def get_toegangscode(self):
        """
        :return: uuid.UUID, het unieke ID van het toegangsbewijs.
        """
        return self.__toegangscode

    def get_gebruiker_id(self):
        """
        :return: uuid.UUID, het unieke ID van de gebruiker.
        """
        return self.__gebruiker_id

    def get_film_id(self):
        """
        :return: str, het IMDB id van de film.
        """
        return self.__film_id

    def get_starttijd(self):
        """
        :return: datetime, de starttijd van de film.
        """
        return self.__starttijd
