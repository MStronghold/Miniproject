from Toegangskaarten import KaartDatabase
from Toegangskaarten import Toegangsbewijs
from Loginsysteem import BezoekerInfo
import datetime

g = BezoekerInfo.BezoekerInfo.nieuw_bezoeker_rnd("Gebruiker1", "Email1", "Wachtwoord1")
k = Toegangsbewijs.Toegangsbewijs.nieuw_toegangsbewijs_str("a0cfe0ba-a5e9-4213-9333-202f3ca56f11", str(g.get_bezoeker_id()), "23", datetime.datetime.now())
print(KaartDatabase.KaartDatabase.kaart_opslaan(k))


print(KaartDatabase.KaartDatabase.kaart_opvragen("a0cfe0ba-a5e9-4213-9333-202f3ca56f11").get_starttijd())
