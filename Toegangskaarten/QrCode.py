import qrcode as _qrcode
import uuid
from Toegangskaarten import Toegangsbewijs


class QrCode:
    @classmethod
    def from_toegangsbewijs(cls, toegangsbewijs):
        """
        :param toegangsbewijs: Toegangsewijs object
        :return: QrCode object
        """
        if type(toegangsbewijs) is not Toegangsbewijs.Toegangsbewijs:
            raise TypeError("id moet een Toegangsbewijs object zijn.")
        return cls.from_uuid(toegangsbewijs.get_gebruiker_id())

    @classmethod
    def from_uuid(cls, id):
        """
        :param id: uuid.UUID object
        :return: QrCode object
        """
        if type(id) is not uuid.UUID:
            raise TypeError("id moet een uuid.UUID object zijn.")
        return cls(uuid.UUID(id))

    def __init__(self, toegangscode):
        """
        :param toegangscode: string object
        :return: QrCode object
        """
        if type(toegangscode) is not str:
            raise TypeError("toegangscode moet een str zijn.")

        _qr = _qrcode.QRCode(version=1, error_correction=_qrcode.ERROR_CORRECT_M)
        _qr.add_data(toegangscode)
        _qr.make()

        self.__qr_img = _qr.make_image()
        self.__data = toegangscode

    def save(self, path):
        """ QR-afbeelding opslaan in path """
        if path is not None:
            self.__qr_img.save(path)

    def get_img(self):
        """
        :return: pil.PilImage object
        """
        return self.__qr_img

    def get_data(self):
        """
        :return: string encoded in de qr code
        """
        return self.__data

# q = QrCode("ddddddddddddddd")
# q.save("qr.png")
