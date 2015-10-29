from tkinter import *
import tkinter.messagebox as tm
from Loginsysteem import BezoekerInfo
from Loginsysteem import Login

class LoginFrame(Frame):

    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Gebruikersnaam  ")
        self.label_2 = Label(self, text="Wachtwoord  ")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)

        self.registreren = Button(self, text="Registreren", command = self.registreren)
        self.registreren.grid(row=2,columnspan=1)

        self.logbtn = Button(self, text="Login", command = self.login)
        self.logbtn.grid(row=2,columnspan=2)

        self.pack()

    def login(self):
        username = self.entry_1.get()
        password = self.entry_2.get()



    def registreren(self):
        username = self.entry_1.get()
        password = self.entry_2.get()

        g = BezoekerInfo.BezoekerInfo.nieuw_bezoeker_rnd("Gebruiker1", "Email1", "Wachtwoord1")
        Login.Login.gebruiker_opslaan(g)

        tm.showinfo("Gebruiker is aangemaakt.")


root = Tk()
lf = LoginFrame(root)
root.mainloop()