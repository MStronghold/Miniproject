from tkinter import *
import tkinter.messagebox as bericht
from Toegangskaarten import KaartDatabase
from klad import API
import uuid


root = Tk()


class startscherm:

    def code_checken(self):
        self.label_1 = Label(root, text="Voer Uw toegangscode in:")
        self.entry_1 = Entry(root)

        self.label_1.pack(side=TOP)
        self.entry_1.pack(side=TOP)

        self.button_1 = Button(root, text="Voer in", command=self.klik)
        self.button_1.pack(side=TOP, pady=4)

    def klik(self):
        Film = self.entry_1.get()

        Info = API.APIrequest(Film)

        if Info == False:
            bericht.showinfo("Toegangscode info", "Dit is geen bestaande toegangscode.")
        else:
            bericht.showinfo(Info)

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

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

        bestelButton = Button(toolbar, text="Film bestellen", command=self.klik)
        bestelButton.pack(side=LEFT, padx=5, pady=10)
        bekijkButton = Button(toolbar, text="Film bekijken", command=self.code_checken)
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
