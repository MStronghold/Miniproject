from Toegangskaarten import KaartDatabase
from Toegangskaarten import Toegangsbewijs
from Loginsysteem import BezoekerInfo
import datetime

# kaart_opslaan testen

gebruiker = BezoekerInfo.BezoekerInfo.nieuw_bezoeker_rnd("Gebruiker1", "Email1", "Wachtwoord1")
gebruiker2 = BezoekerInfo.BezoekerInfo.nieuw_bezoeker_rnd("Gebruiker2", "Email2", "Wachtwoord2")

kaart = Toegangsbewijs.Toegangsbewijs.nieuw_toegangsbewijs_str("a0cfe0ba-a5e9-4213-9333-202f3ca56f20", str(gebruiker2.get_bezoeker_id()), "234", datetime.datetime.now())
kaart2 = Toegangsbewijs.Toegangsbewijs.nieuw_toegangsbewijs_str("a0cfe0ba-a5e9-4213-9333-202f3ca56f21", str(gebruiker2.get_bezoeker_id()), "2345", datetime.datetime.now())
print(KaartDatabase.KaartDatabase.kaart_opslaan(kaart))
print(KaartDatabase.KaartDatabase.kaart_opslaan(kaart2))


# kaart_opvragen testen

kaart_opgevraagd = KaartDatabase.KaartDatabase.kaart_opvragen("a0cfe0ba-a5e9-4213-9333-202f3ca56f13")
kaart_opgevraagd2 = KaartDatabase.KaartDatabase.kaart_opvragen("a0cfe0ba-a5e9-4213-9333-202f3ca56f20")

print(kaart_opgevraagd2.get_gebruiker_id())


# kaarten_opvragen_gebruiker testen

kaarten_opgevraagd_gebruiker = KaartDatabase.KaartDatabase.kaarten_opvragen_gebruiker("4505558c-de33-4a66-84e7-336d0090992b")
print(kaarten_opgevraagd_gebruiker)

for kaarten in kaarten_opgevraagd_gebruiker:
    print(str(kaarten.get_toegangscode()))

# kaarten_opvragen_film testen

kaarten_opgevraagd_film = KaartDatabase.KaartDatabase.kaarten_opvragen_film("23")
print(kaarten_opgevraagd_film)

for kaarten in kaarten_opgevraagd_film:
    print("Toegangscode: " + str(kaarten.get_toegangscode()) + " Gebruiker: " + str(kaarten.get_gebruiker_id()))

# kaart_verwijderen testen

print(KaartDatabase.KaartDatabase.kaart_verwijderen("a0cfe0ba-a5e9-4213-9333-202f3ca56f20"))


# QRcode testen

kaart_opgevraagd.genereer_qr("qr.png")
