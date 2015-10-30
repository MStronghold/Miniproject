from tkinter import *
import tkinter.messagebox as bericht
from klad import API


root = Tk()


class startscherm:

    # ***** Kijken of klikken werkt *****

    def klik(selfs):
        print("klikken werkt!")

    # ***** Film invoer deel *****

    def film_checken(self):

        if self.knop_drukken == 0:
            self.label_1 = Label(root, text="Voer een titel in:")
            self.entry_1 = Entry(root)

            self.label_1.pack(side=TOP)
            self.entry_1.pack(side=TOP)

            self.button_1 = Button(root, text="Zoeken", command=self.invoeren)
            self.button_1.pack(side=TOP, pady=4)

            self.knop_drukken += 1

    def invoeren(self):
        film = self.entry_1.get()

        info = API.APIrequest(film)

        if info['Response'] == ['False']:
            bericht.showinfo("Film info", "Dit is geen bestaande film.")
        else:
            print(info)


    # ***** Hoofdpagina *****

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.knop_drukken = 0

        menu = Menu(root)
        root.config(menu=menu)

        # ***** Main Menu *****

        filemenu = Menu(menu)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New Project...", command=self.klik)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=exit)

        # ***** Toolbar *****

        toolbar = Frame(root, bg="#A5110D")

        bekijkbutton = Button(toolbar, text="Film bekijken", command=self.film_checken)
        bekijkbutton.pack(side=LEFT, padx=5, pady=10)

        toolbar.pack(side=TOP, fill=X)

        # ***** Status Bar *****

        self.status = Label(root, text="Statusbar...", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    photo = PhotoImage(file="Studio100.png")
    label = Label(root, image=photo)
    label.pack(fill=X)

startscherm(root)

root.mainloop()