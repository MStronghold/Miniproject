import tkinter.messagebox as bericht
from tkinter import *

from API import API

toor = Tk()


class StartScherm:

    # ***** Kijken of klikken werkt *****

    def klik(self):
        print("gff")

    def leegmaken(self):
        for i in verwijderdregels:
            i.destroy()

    # ***** Film invoer deel ******

    def film_checken(self):

        if self.knop_drukken == 0:
            self.label_1 = Label(toor, text="Voer een titel in:")
            self.entry_1 = Entry(toor)

            self.label_1.pack(side=TOP)
            self.entry_1.pack(side=TOP)

            self.button_1 = Button(toor, text="Zoeken", command=self.invoeren)
            self.button_1.pack(side=TOP, pady=4)

            self.knop_drukken += 1

    def invoeren(self):
        global informatie, verwijderdregels
        self.leegmaken()
        verwijderdregels = []
        film = self.entry_1.get()
        info = API.APIrequest(film)

        if info['Response'] == ['False']:
            bericht.showinfo("Film info", "Dit is geen bestaande film.")
        else:
            for regel in info.items():
                informatie = Label(toor, text=regel, bg="white")
                informatie.pack(anchor=W)
                verwijderdregels.append(informatie)


    # ***** Hoofdpagina *****

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.knop_drukken = 0

        menu = Menu(toor)
        toor.config(menu=menu)

        # ***** Main Menu *****

        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Project...", command=self.klik)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=exit)

        # ***** Toolbar *****

        toolbar = Frame(toor, bg="#A5110D")

        bekijkbutton = Button(toolbar, text="Film bekijken", command=self.film_checken)
        bekijkbutton.pack(side=LEFT, padx=5, pady=10)

        toolbar.pack(side=TOP, fill=X)

        # ***** Status Bar *****

        self.status = Label(toor, text="Statusbar...", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    photo = PhotoImage(file="Studio100.png")
    label = Label(toor, image=photo)
    label.pack(fill=X)

StartScherm(toor)

toor.mainloop()
