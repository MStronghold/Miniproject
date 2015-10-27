import BezoekerInfo


class Login():

    gebruikers = []

    @classmethod
    def gebruikersnaam_bestaat(cls, gebruikersnaam):
        """
        :param gebruikersnaam: gebruikersnaam (string)
        :return: BezoekerInfo.BezoekerInfo object als de gebruiker bestaat. False als de gebruiker niet bestaat.
        """
        if type(gebruikersnaam) is not str:
            raise TypeError("gebruikersnaam moet een string zijn.")
        elif len(gebruikersnaam) == 0:
            raise ValueError("Gebruikersnaam mag niet leeg zijn.")

        for i in cls.gebruikers:
            if i.get_gebruikersnaam() == gebruikersnaam:
                return i
        return False

    @classmethod
    def email_bestaat(cls, email):
        """
        :param email: email (string)
        :return: BezoekerInfo.BezoekerInfo object als het mailadres bestaat. False als het mailadres niet bestaat.
        """
        if type(email) is not str:
            raise TypeError("email moet een string zijn.")
        elif len(email) == 0:
            raise ValueError("email mag niet leeg zijn.")

        for i in cls.gebruikers:
            if i.get_email() == email:
                return i
        return False

    @classmethod
    def nieuwe_gebruiker(cls, gebruikersnaam, email, wachtwoord):
        """
        :param gebruikersnaam: Gebruikersnaam (string)
        :param email: Email (string)
        :param wachtwoord: Wachtwoord (string)
        :return: BezoekerInfo object als de gebruiker successvol is aangemaakt, False als het niet is gelukt.
        """
        if type(gebruikersnaam) is not str:
            raise TypeError("gebruikersnaam moet een string zijn.")
        elif len(gebruikersnaam) == 0:
            raise ValueError("Gebruikersnaam mag niet leeg zijn.")

        if type(email) is not str:
            raise TypeError("email moet een string zijn.")
        elif len(email) == 0:
            raise ValueError("email mag niet leeg zijn.")

        if type(wachtwoord) is not str:
            raise TypeError("wachtwoord moet een string zijn.")
        elif len(wachtwoord) == 0:
            raise ValueError("wachtwoord mag niet leeg zijn.")

        if cls.gebruikersnaam_bestaat(gebruikersnaam) or cls.email_bestaat(email):
            return False

        n_gebruiker = BezoekerInfo.BezoekerInfo.nieuw_bezoeker_rnd(gebruikersnaam, email, wachtwoord)
        cls.gebruikers.append(n_gebruiker)
        return n_gebruiker

    @classmethod
    def check_gebruiker(cls, gebruikersnaam, wachtwoord):
        """
        :param gebruikersnaam: gebruikersnaam (string)
        :param wachtwoord: wachtwoord (string)
        :return:
        """
        for i in cls.gebruikers:
            if i.get_gebruikersnaam() == gebruikersnaam and i.get_wachtwoord() == wachtwoord:
                return i
        return False

    @classmethod
    def zoek_email(cls, gebruikersnaam):
        """
        :param gebruikersnaam: gebruikersnaam (string)
        :return: Mailadres (string) als het mailadres gevonden is, False als het niet gevonden is.
        """
        for i in cls.gebruikers:
            if i.get_gebruikersnaam() == gebruikersnaam:
                return i.get_email()
        return False

# Voorbeeld:
# Login.nieuwe_gebruiker("testgebruiker", "mijnmail@example.com", "123456")
# Login.nieuwe_gebruiker("gebruikertest", "mail2@example.com", "654321")
# print(Login.zoek_email("gebruikertest"))

