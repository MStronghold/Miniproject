from Loginsysteem import BezoekerInfo
from Loginsysteem import Login

# Nieuwe gebruiker aanmaken
g = BezoekerInfo.BezoekerInfo.nieuw_bezoeker_rnd("Gebruiker1", "Email1", "Wachtwoord1")
print(g.to_dict())

# Gebruiker proberen op te slaan in database
Login.Login.gebruiker_opslaan(g)

# Wachtwoord opvragen van een gebruiker
print(Login.Login.gebruiker_opvragen("Gebruiker1").get_wachtwoord())
print(Login.Login.gebruiker_opvragen("Email1").get_wachtwoord())

# Email opvragen van een gebruiker met het gebruikersnaam
print(Login.Login.gebruiker_opvragen("Gebruiker1").get_email())

# ID opvragen van gebruiker
print(Login.Login.gebruiker_opvragen("Email1").get_bezoeker_ID())

# Gebruiker proberen op te slaan en checken of de gebruikersnaam al in gebruik is.
if Login.Login.gebruiker_opslaan(BezoekerInfo.BezoekerInfo.nieuw_bezoeker_rnd("Gebruiker1", "Email2", "Wachtwoord2")) == 1:
    print("Gebruikersnaam al in gebruik")

# ~~ en checken of het emailadres al gebruikt is
if Login.Login.gebruiker_opslaan(BezoekerInfo.BezoekerInfo.nieuw_bezoeker_rnd("Gebruiker1", "Email2", "Wachtwoord2")) == 2:
    print("Emailadres al in gebruik")

# Gebruiker verwijderen uit de database
Login.Login.gebruiker_verwijderen(g.get_bezoeker_id())

# Info aanpassen van bestaande gebruiker
print(g.to_dict())
g.set_gebruikersnaam("MijnGebruikersnaam")
g.set_wachtwoord("MijnWachtwoord")
print(g.to_dict())
Login.Login.gebruiker_opslaan(g, True)
