from tkinter import *

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