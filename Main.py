from LoginInterface import LoginGui

# Open LoginGui
_LoginGui_lst = LoginGui.Login_Frame.open_interface()
_LoginGui_root = _LoginGui_lst[0]
_LoginGui_class = _LoginGui_lst[1]
_LoginGui_root.mainloop()

_ingelogde_gebruiker = _LoginGui_class.gebruiker
print(_ingelogde_gebruiker.get_gebruikersnaam())
