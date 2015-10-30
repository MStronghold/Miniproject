from tkinter import *
def messageWindow():
    win = Toplevel()
    message = "This is the child window"
    Label(win, text=message).pack()
    Button(win, text='OK', command=win.destroy).pack()




# ---------------------------------------- FIRST window ----------------------------------------
from tkinter import *
import tkinter.messagebox as bericht
from Loginsysteem import BezoekerInfo
from Loginsysteem import Login

class Login_Frame(Frame):

    def __init__(self, master):
        super().__init__(master)

        # ***** Tekst *****
        self.label_1 = Label(self, text="Gebruikersnaam: ")
        self.label_2 = Label(self, text="Wachtwoord: ")
        self.label_3 = Label(self, text="E-mail: ")

        # ***** Input velden *****
        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")
        self.entry_3 = Entry(self)

        # ***** De opmaak van de input velden *****
        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.label_3.grid(row=2, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)
        self.entry_3.grid(row=2, column=1)

        # ***** Functie checkbox *****
        self.checked = False
        def checkbox():
            self.checked = not self.checked

        # ***** Checkbox en login knoppen *****
        self.checkbox_1 = Checkbutton(self, text="Aanbieder", command = checkbox)
        self.button_1 = Button(self, text="Registreren", command = self.registreren)
        self.button_2 = Button(self, text="Aanmelden", command = self.aanmelden)

        # ***** De opmaak van de checkbox en login knoppen *****
        self.checkbox_1.grid(row=3,columnspan=1)
        self.button_1.grid(row=4)
        self.button_2.grid(row=4, column=1)

        self.pack()

    def aanmelden(self):
        # ***** Ophalen van gegevens tekstvakken *****
        gebruikersnaam = self.entry_1.get()
        wachtwoord = self.entry_2.get()
        email = self.entry_3.get()

        # ***** Gegevens opvragen uit database *****
        gebruiker = Login.Login.gebruiker_opvragen(gebruikersnaam)

        '''
        Als de gebruiker niet bestaat geeft hij een foutmelding en stopt de functie.
        Als de gebruiker wel bestaat checkt hij of de gegevens uit database het zelfde zijn als de input.
        Als dit het zelfde is ben je ingelogd anders geeft hij een foutmelding.
        '''

        if gebruiker == False:
            bericht.showerror("Login", "Dit is geen bestaande gebruiker.")
        else:
            wachtwoord_database = gebruiker.get_wachtwoord()
            if gebruiker.get_gebruikersnaam() == gebruikersnaam and wachtwoord_database == wachtwoord:
                messageWindow()
            elif wachtwoord_database != wachtwoord:
                bericht.showerror("Login", "Wachtwoord is onjuist.")
            else:
                bericht.showerror("Login", "Wachtwoord is onjuist.")

    def registreren(self):
        # ***** Ophalen van gegevens tekstvakken *****
        gebruikersnaam = self.entry_1.get()
        wachtwoord = self.entry_2.get()
        email = self.entry_3.get()

        '''
        Minimaal 3 karakters per veld anders komt er een foutmelding en stopt de functie.
        Hij maakt de gebruiker aan en kijkt wat voor output deze actie geeft.
        Als de output een fout betreft die gedefineerd is in login.py dan word hier een foutmelding van getoond.
        '''

        if len(gebruikersnaam) < 3 or len(wachtwoord) < 3 or len(email) < 3:
            bericht.showerror("Login", "Minimaal 3 karakters per veld.")
        else:
            nieuwe_gebruiker = BezoekerInfo.BezoekerInfo.nieuw_bezoeker_rnd(gebruikersnaam, email, wachtwoord, self.checked)
            login_status = Login.Login.gebruiker_opslaan(nieuwe_gebruiker)

            if login_status == 0:
                bericht.showerror("Login", "Gebruiker aanmaken is niet gelukt.")
            elif login_status == 1:
                bericht.showerror("Login", "Gebruikersnaam is al in gebruik.")
            elif login_status == 2:
                bericht.showerror("Login", "E-mail is al in gebruik.")
            elif login_status == 3:
                bericht.showinfo("Login", "Gebruiker succesvol aangemeld.")

root = Tk()
lf = Login_Frame(root)
frame = Frame(root, width=250)
frame.pack()
root.mainloop()