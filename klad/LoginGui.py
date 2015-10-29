from tkinter import *
import tkinter.messagebox as bericht
from Loginsysteem import BezoekerInfo
from Loginsysteem import Login

class Login_Frame(Frame):

    def __init__(self, master):
        super().__init__(master)

        self.label_1 = Label(self, text="Gebruikersnaam: ")
        self.label_2 = Label(self, text="Wachtwoord: ")
        self.label_3 = Label(self, text="E-mail: ")

        self.entry_1 = Entry(self)
        self.entry_2 = Entry(self, show="*")
        self.entry_3 = Entry(self)

        self.label_1.grid(row=0, sticky=E)
        self.label_2.grid(row=1, sticky=E)
        self.label_3.grid(row=2, sticky=E)
        self.entry_1.grid(row=0, column=1)
        self.entry_2.grid(row=1, column=1)
        self.entry_3.grid(row=2, column=1)

        self.checked = False

        def test():
            self.checked = not self.checked


        self.checkbox_1 = Checkbutton(self, text="Aanbieder", command = test)
        self.checkbox_1.grid(row=3,columnspan=1)

        self.button_1 = Button(self, text="Registreren", command = self.registreren)
        self.button_1.grid(row=4)

        self.button_2 = Button(self, text="Aanmelden", command = self.aanmelden)
        self.button_2.grid(row=4, column=1)

        self.pack()

    def aanmelden(self):
        gebruikersnaam = self.entry_1.get()
        wachtwoord = self.entry_2.get()
        email = self.entry_3.get()

        gebruiker = Login.Login.gebruiker_opvragen(gebruikersnaam)
        print(gebruiker)

        if gebruiker == False:
            bericht.showinfo("Login info", "Dit is geen bestaande gebruiker.")
        else:
            wachtwoord_database = gebruiker.get_wachtwoord()
            if gebruiker.get_gebruikersnaam() == gebruikersnaam and wachtwoord_database == wachtwoord:
                startscherm()
            elif wachtwoord_database != wachtwoord:
                bericht.showinfo("Login info", "Wachtwoord is niet geldig.")
            else:
                print("Login ongeldig.")

    def registreren(self):
        gebruikersnaam = self.entry_1.get()
        wachtwoord = self.entry_2.get()
        email = self.entry_3.get()


        nieuwe_gebruiker = BezoekerInfo.BezoekerInfo.nieuw_bezoeker_rnd(gebruikersnaam, email, wachtwoord, self.checked)
        login_status = Login.Login.gebruiker_opslaan(nieuwe_gebruiker)

        if login_status == 0:
            bericht.showinfo("Login info", "Gebruiker aanmaken is niet gelukt.")
        elif login_status == 1:
            bericht.showinfo("Login info", "Gebruikersnaam is al in gebruik.")
        elif login_status == 2:
            bericht.showinfo("Login info", "E-mail is al in gebruik.")
        elif login_status == 3:
            bericht.showinfo("Login info", "Gebruiker succesvol aangemeld.")


def startscherm():

    def klik():
        print("Klikken werkt!")

    root = Tk()


    menu = Menu(root)
    root.config(menu=menu)

    # ***** Main Menu *****

    fileMenu = Menu(menu)
    menu.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New Project...", command=klik)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=exit)




    # ***** Toolbar *****

    toolbar = Frame(root, bg="#A5110D")

    bestelButton = Button(toolbar, text="Film bestellen", command=klik)
    bestelButton.pack(side=LEFT, padx=5, pady=10)
    bekijkButton = Button(toolbar, text="Film bekijken", command=klik)
    bekijkButton.pack(side=LEFT, padx=5, pady=10)

    toolbar.pack(side=TOP, fill=X)

    # ***** Status Bar *****

    status = Label(root, text="Statusbar...", bd=1, relief=SUNKEN, anchor=W)
    status.pack(side=BOTTOM, fill=X)

    photo = PhotoImage(file="Studio100.png")
    label = Label(root, image=photo)
    label.pack(fill=X)

    frame = Frame(root, width=1280, height= 720, bg="#FFF")
    frame.pack(fill=X)

    root.mainloop()

root = Tk()
lf = Login_Frame(root)
frame = Frame(root, width=250)
frame.pack()
root.mainloop()