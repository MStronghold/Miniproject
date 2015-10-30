from tkinter import *
import tkinter.messagebox as bericht
from klad import API
import uuid


root = Tk()


class startscherm:


    def klik(selfs):
        print("klikken werkt!")

    def film_checken(self):

        if self.knop_drukken == 0:
            self.label_1 = Label(root, text="Voer een titel in:")
            self.entry_1 = Entry(root)

            self.label_1.pack(side=TOP)
            self.entry_1.pack(side=TOP)

            self.button_1 = Button(root, text="Zoeken", command=self.filminvoeren)
            self.button_1.pack(side=TOP, pady=4)

            self.knop_drukken += 1

    def filminvoeren(self):
        filmzoeken = self.entry_1.get()

        film = API.APIrequest(filmzoeken)

        if film == False:
            bericht.showinfo("Film info", "Dit is geen bestaande film.")
        elif film == True:
            print(APIrequest('robin hood'))


    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.knop_drukken = 0

        menu = Menu(root)
        root.config(menu=menu)

        # ***** Main Menu *****

        fileMenu = Menu(menu)
        menu.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="New Project...", command=self.klik)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=exit)




        # ***** Toolbar *****

        toolbar = Frame(root, bg="#A5110D")

        bekijkButton = Button(toolbar, text="Film bekijken", command=self.film_checken)
        bekijkButton.pack(side=LEFT, padx=5, pady=10)

        toolbar.pack(side=TOP, fill=X)

        # ***** Status Bar *****

        self.status = Label(root, text="Statusbar...", bd=1, relief=SUNKEN, anchor=W)
        self.status.pack(side=BOTTOM, fill=X)

    photo = PhotoImage(file="Studio100.png")
    label = Label(root, image=photo)
    label.pack(fill=X)



startscherm(root)


root.mainloop()





