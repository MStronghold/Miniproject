import tkinter.messagebox as bericht
from tkinter import *

from API import API

class StartScherm(Frame):

    @classmethod
    def open_interface(cls, gebruiker):
        root = Tk()
        frame = Frame(root)
        frame.pack()
        lf = cls(root, gebruiker)
        return [root, lf]

    # ***** Kijken of klikken werkt *****

    def klik(self):
        print("Het werkt!")

    def leegmaken(self):
        try:
            for i in verwijderdregels:
                i.destroy()
        except:
            print("")

    # ***** Film invoer deel ******

    def film_checken(self):

        if self.knop_drukken == 0:
            self.label_1 = Label(self._master, text="Voer een titel in:")
            self.entry_1 = Entry(self._master)

            self.label_1.pack(side=TOP)
            self.entry_1.pack(side=TOP)

            self.button_1 = Button(self._master, text="Zoeken", command=self.invoeren)
            self.button_1.pack(side=TOP, pady=4)

            self.knop_drukken += 1

    def invoeren(self):
        global informatie, verwijderdregels
        self.leegmaken()
        verwijderdregels = []
        film = self.entry_1.get()
        info = API.APIrequest(film)

        if "Movie not found!" in str(info):
            bericht.showerror("Film info", "Dit is geen bestaande film.")
        else:
            for regel in info.items():
                def labels(a):
                    if a in regel:
                        regelnetjes = str(regel).replace("(","").replace("'","").replace(")","").replace(",",":")
                        informatie = Label(self._master, text=regelnetjes, bg="white",font=("Helvetica", 16))
                        informatie.pack(anchor=W)
                        verwijderdregels.append(informatie)
                labels("Title")
                labels("Actors")
                labels("Plot")
                labels("Director")
                labels("Language")
                labels("imdbRating")
                labels("Released")
                labels("Genre")
                labels("Runtime")
                labels("Year")

    # ***** Hoofdpagina *****

    def __init__(self, master, gebruiker):
        super().__init__(master)
        self._master = master
        self._gebruiker = gebruiker

        self.photo = PhotoImage(file=".\MainInterface\Studio100.png")
        self.label = Label(self._master, image=self.photo)
        self.label.pack(fill=X)

        self.knop_drukken = 0

        menu = Menu(self._master)
        self._master.config(menu=menu)

        # ***** Main Menu *****

        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Project...", command=self.klik)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=exit)

        # ***** Toolbar *****

        toolbar = Frame(self._master, bg="#A5110D")

        bekijkbutton = Button(toolbar, text="Film bekijken", command=self.film_checken)
        bekijkbutton.pack(side=LEFT, padx=5, pady=10)

        toolbar.pack(side=TOP, fill=X)

        # ***** Status Bar *****

        self.status = Label(self._master, text="Statusbar...", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)
